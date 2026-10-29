---
name: ackos-control
description: Use when a requested repository or external-state mutation must be authorized, executed, and verified through ackOS.
---

# ackOS-controlled changes

Use this skill when the task requires a state-changing operation to pass through ackOS. Wingman remains the caller and coordinator; ackOS is the authority for authorization, execution lifecycle, independent verification, recovery, and commitment.

## Hard boundary

1. Confirm that the user's requested change, target resource, scope, and prohibited actions are explicit.
2. Read the target system's instructions and security guidance. For repository-backed operations, inspect the current branch/head and relevant file before proposing the mutation.
3. For file replacements through ackos-api, use Wingman's `tooling/ackos_api_change.py` client. It performs the documented HTTP sequence: `POST /v1/observations`, then `POST /v1/changes` with the opaque token returned by the first request.
4. Require the API base URL, bearer credential, and repository identifier to be configured out-of-band in the runtime environment. Use `ACKOS_API_BASE_URL`, `ACKOS_API_BEARER_TOKEN`, and `ACKOS_API_REPOSITORY_ID`; never put credentials in files, arguments, logs, or chat. The repository identifier must be one configured on the API server; never substitute an arbitrary filesystem path.
5. Do not treat this skill, the HTTP client, a GitHub connector, or the synthetic `cmd/ackos-mcp` demo as execution authority. The authenticated API must be connected to the provider-backed ackOS runtime.
6. Never perform the protected mutation directly through ordinary file editing, Git commands, GitHub Contents/Write APIs, or Terraform as a fallback around ackOS.
7. If the API service, credentials, repository mapping, or supported request path is unavailable, stop before the mutation and report the exact missing integration. Do not invent resource IDs, observations, fingerprints, concurrency tokens, or desired-state encodings.
8. Do not push, merge, release, or change production/infrastructure state without the specific human authorization required by the target system and task.

## Prepare the transition

Use the configured provider's supported resource model. Before calling the client, establish the applicable values:

- The configured API repository identifier, target branch, and repository-relative path.
- The exact desired file bytes, prepared as a local content file.
- The allowed file mode (`100644` by default; use `100755` only when the file is intentionally executable).
- The configured API endpoint and bearer credential, supplied through the trusted runtime environment.

Invoke the client from the Wingman repository root:

```sh
python3 tooling/ackos_api_change.py \
  --branch <configured-branch> \
  --path <existing-repository-relative-file> \
  --content-file <file-containing-exact-desired-bytes>
```

The client obtains the fresh observation and opaque concurrency token from the API; callers must never construct or reuse them. It submits the token immediately with the requested content. It does not automatically retry failures. A stale/expired observation or HTTP 409 is not success: stop, re-inspect the current state, and re-evaluate authorization before another attempt.

## Execute and verify

1. Submit the smallest in-scope transition through the configured ackos-api client only.
2. Treat denied, stale, failed, timed-out, cancelled, or ambiguous results as **not successful**.
3. Require the API/ackOS response to report successful independent verification and commitment. Do not infer success from an HTTP transport status alone.
4. Independently inspect the resulting provider state when a supported read path is available. For Git, confirm the expected branch/ref, resulting commit, exact target content, and absence of unrelated changes.
5. If verification or execution fails, follow the existing ackOS recovery lifecycle. Do not invent a successful state or perform direct compensating writes.

## Terraform and infrastructure safety

- For repository-only Terraform tests, use a disposable local clone and a dedicated test branch.
- Never run `terraform apply`, provision cloud resources, or modify AWS infrastructure as part of a Git integration test.
- Prefer a harmless documentation/comment-only change to an existing tracked file. Do not change resource addresses, counts, credentials, or infrastructure arguments for a smoke test.
- Run formatting/validation only when the required tooling and initialization can be used safely; clearly distinguish checks that ran from checks that did not.

## Required report

Report the result as **PASS**, **PARTIAL**, or **BLOCKED**. Include the configured API service identity (without secrets), target repository identifier and scope, initial and final state identifiers, changed paths when applicable, ackOS verification/commit result, checks actually run, and limitations. Never claim end-to-end success based only on a successful file edit, unit test, proposed patch, or ordinary GitHub write.

## Security note

This skill is model-facing workflow guidance, not an enforcement boundary. The executable ackOS kernel and provider-backed integration must enforce authorization and own execution and verification. If that integration is not actually connected, prepare a proposal and report the blocker; do not perform the side effect directly.
