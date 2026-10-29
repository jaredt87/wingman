# ackOS API HTTP client

Use `tooling/ackos_api_change.py` to submit an existing-file replacement through the configured `ackos-api` service. The client sends an authenticated observation request first, then uses the opaque returned token for the change request. It does not write Git state directly.

## Configuration

Set these environment variables in the trusted agent/runtime environment; never put credentials in the repository or command-line arguments:

- `ACKOS_API_BASE_URL`: the API origin/base URL (HTTPS required except loopback development).
- `ACKOS_API_BEARER_TOKEN`: bearer credential for ackos-api.
- `ACKOS_API_REPOSITORY_ID`: repository identifier configured on the API server (not a filesystem path).

Example for a local test service:

```sh
export ACKOS_API_BASE_URL=http://127.0.0.1:8080
export ACKOS_API_BEARER_TOKEN='provided-out-of-band'
export ACKOS_API_REPOSITORY_ID=terraform
python3 tooling/ackos_api_change.py --branch main --path README.md --content-file /tmp/desired-README.md
```

The target file must already exist in the configured repository and branch. The client never retries a failed or stale request automatically. A stale observation (HTTP 409) requires fresh inspection and human re-evaluation before another attempt.

The API/ackOS response is the authority for whether the change was independently verified and committed. Do not infer success from a successful HTTP transport alone, and do not use Git, GitHub write APIs, or Terraform as a fallback.
