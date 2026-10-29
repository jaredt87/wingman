#!/usr/bin/env python3
"""Submit a file replacement through the authenticated ackos-api HTTP contract.

This client never writes Git objects or invokes Git/GitHub/Terraform directly.
The API and ackOS remain responsible for observation, authorization, execution,
verification, and commitment.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import PurePosixPath
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _configuration() -> tuple[str, str, str]:
    base_url = os.environ.get("ACKOS_API_BASE_URL", "").strip().rstrip("/")
    bearer = os.environ.get("ACKOS_API_BEARER_TOKEN", "")
    repository_id = os.environ.get("ACKOS_API_REPOSITORY_ID", "").strip()
    if not base_url or not bearer or not repository_id:
        raise ValueError(
            "Set ACKOS_API_BASE_URL, ACKOS_API_BEARER_TOKEN, and "
            "ACKOS_API_REPOSITORY_ID in the environment."
        )

    parsed = urlsplit(base_url)
    local_hosts = {"localhost", "127.0.0.1", "::1"}
    if parsed.scheme != "https" and not (
        parsed.scheme == "http" and parsed.hostname in local_hosts
    ):
        raise ValueError("ACKOS_API_BASE_URL must use HTTPS (HTTP is allowed only for loopback).")
    if not parsed.netloc or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("ACKOS_API_BASE_URL must be an origin/base path without credentials, query, or fragment.")
    return base_url, bearer, repository_id


def _post_json(base_url: str, bearer: str, route: str, payload: dict) -> dict:
    url = f"{base_url}{route}"
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    request = Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {bearer}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    opener = build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=30) as response:
            raw = response.read()
            status = response.status
    except HTTPError as exc:
        # Do not echo server bodies: they may contain sensitive request details.
        raise RuntimeError(f"ackos-api returned HTTP {exc.code} for {route}; no retry was attempted.") from None
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"ackos-api request to {route} failed ({type(exc).__name__}); no retry was attempted.") from None

    if status < 200 or status >= 300:
        raise RuntimeError(f"ackos-api returned HTTP {status} for {route}; no retry was attempted.")
    try:
        result = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise RuntimeError(f"ackos-api returned invalid JSON for {route}.") from None
    if not isinstance(result, dict):
        raise RuntimeError(f"ackos-api returned an unexpected response for {route}.")
    return result


def _validate_path(path: str) -> str:
    candidate = PurePosixPath(path)
    if not path or candidate.is_absolute() or any(part in ("", ".", "..") for part in path.split("/")):
        raise ValueError("Path must be a normalized repository-relative file path.")
    if "\\" in path:
        raise ValueError("Path must use POSIX separators.")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Replace an existing tracked file through ackos-api and ackOS."
    )
    parser.add_argument("--branch", required=True, help="Configured target branch name")
    parser.add_argument("--path", required=True, help="Existing repository-relative file path")
    parser.add_argument("--content-file", required=True, help="Local file containing the exact desired bytes")
    parser.add_argument("--mode", choices=("100644", "100755"), default="100644")
    args = parser.parse_args(argv)

    try:
        base_url, bearer, repository_id = _configuration()
        path = _validate_path(args.path)
        if not args.branch.strip() or args.branch.startswith("-"):
            raise ValueError("Branch must be a non-empty branch name.")
        with open(args.content_file, "rb") as source:
            content = source.read()

        observation = _post_json(
            base_url,
            bearer,
            "/v1/observations",
            {"repository_id": repository_id, "branch": args.branch, "path": path},
        )
        token = observation.get("observation_token")
        if not isinstance(token, str) or not token:
            raise RuntimeError("ackos-api observation response did not contain an observation_token.")
        # The token is opaque and secret-like: use it only for the second request.
        result = _post_json(
            base_url,
            bearer,
            "/v1/changes",
            {
                "observation_token": token,
                "mode": args.mode,
                "content_base64": base64.b64encode(content).decode("ascii"),
            },
        )
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ackos-api change failed: {exc}", file=sys.stderr)
        return 1

    # Deliberately omit response bodies and token fields from output.
    commit = result.get("commit_id") or result.get("commit_sha")
    if isinstance(commit, str) and commit:
        print(f"ackos-api change completed; ackOS reported success (commit {commit}).")
    else:
        print("ackos-api change completed; ackOS reported success.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
