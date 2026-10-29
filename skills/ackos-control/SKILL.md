---
name: ackos-control
description: Use when a requested repository or external-state mutation must be authorized, executed, and verified through ackOS.
---

# ackOS-controlled changes

Use this skill when the task requires a state-changing operation to pass through ackOS. Wingman remains the caller and coordinator; ackOS is the authority for authorization, execution lifecycle, independent verification, recovery, and commitment.

## Hard boundary

1. Confirm that the user's requested change, target resource, scope, and prohibited actions are explicit.
2. Read the target system's instructions and security guidance. For repository-backed operations, inspect the current branch/head and relevant file before proposing the mutation.
3. **Require an actual callable `ackos_control` MCP tool connected to a real, configured, provider-backed ackOS server** that owns authorization, execution, independent verification, recovery, and commitment. This is a mandatory execution gate for every protected mutation.
4. The HTTP client in this repository is not a substitute for that integration and must not be invoked directly to perform a protected mutation. It may be used only as an internal transport by an already configured `ackos_control` integration, if that integration explicitly supports and authorizes this transport. The fact that ackos-api delegates to ackOS does not itself satisfy the callable-tool gate.
5. If the callable tool, provider-backed server, supported input-building/observation path, or configured transport is unavailable, stop before the mutation and report the exact missing integration. Do not invent resource IDs, observations, fingerprints, concurrency tokens, or desired-state encodings.
6. Do not treat this skill, the HTTP client, a GitHub connector, or the synthetic `cmd/ackos-mcp` demo as execution authority.
7. Never perform the protected mutation directly through ordinary file editing, Git commands, GitHub Contents/Write APIs, a direct invocation of `tooling/ackos_api_change.py`, or Terraform as a fallback around ackOS.
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
