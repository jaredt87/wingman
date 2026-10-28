---
name: ackos-control
description: Use when a requested repository or external-state mutation must be authorized, executed, and verified through ackOS.
---

# ackOS-controlled changes

Use this skill when the task requires a state-changing operation to pass through ackOS. Wingman remains the caller and coordinator; ackOS is the authority for authorization, execution lifecycle, independent verification, recovery, and commitment.

## Hard boundary

1. Confirm that the user’s requested change, target repository, branch, path, and prohibited actions are explicit.
2. Read the target repository’s instructions and security guidance. Inspect the current branch/head and relevant file before proposing the mutation.
3. Require an actual callable `ackos_control` MCP tool connected to a provider-backed ackOS server that owns the executor and independent verifier.
4. Do not treat a skill, a model decision, a GitHub connector, or the synthetic `cmd/ackos-mcp` demo as proof of provider-backed execution.
5. Never perform the protected mutation directly through ordinary file editing, Git commands, GitHub Contents/Write APIs, or another side-effecting tool as a fallback around ackOS.
6. If the real tool/server or its supported input-building/observation path is unavailable, stop before the mutation and report the exact missing integration. Do not invent resource IDs, observations, fingerprints, concurrency tokens, or desired-state encodings.
7. Do not push, merge, release, or change production/infrastructure state without the specific human authorization required by the target repository and task.

## Prepare the transition

Before calling ackOS, establish:

- The exact configured provider resource and its permitted repository root, full branch ref, and repository-relative path.
- The provider-supported subject/resource identity.
- A fresh observation and concurrency token from the supported provider flow.
- The exact desired state in the encoding required by that provider.
- The authority lifetime requested by the caller, if applicable.

Use provider-owned helpers or a documented observation interface to construct these values. Never derive an authorization observation from the proposed result or reuse a stale observation. If the MCP interface does not expose enough supported information to prepare a valid request, treat that as a blocking integration gap—not permission to bypass ackOS.

## Execute and verify

1. Submit the smallest in-scope transition through `ackos_control` only.
2. Treat a denied, stale, failed, timed-out, cancelled, or ambiguous result as **not successful**.
3. Do not retry with stale values. Obtain a fresh provider observation and re-evaluate authorization before a new attempt.
4. Require ackOS to report successful independent verification and commitment.
5. Independently inspect the resulting Git/provider state when a read path is available. Confirm the expected branch/ref, resulting commit or state identifier, exact target content, and absence of unrelated changes.
6. If verification or execution fails, follow the existing ackOS recovery lifecycle. Do not invent a successful state or perform direct compensating writes.

## Terraform and infrastructure safety

- For repository-only Terraform tests, use a disposable local clone and a dedicated test branch.
- Never run `terraform apply`, provision cloud resources, or modify AWS infrastructure as part of a Git integration test.
- Prefer a harmless documentation/comment-only change to an existing tracked file. Do not change resource addresses, counts, credentials, or infrastructure arguments for a smoke test.
- Run formatting/validation only when the required tooling and initialization can be used safely; clearly distinguish checks that ran from checks that did not.

## Required report

Report the result as **PASS**, **PARTIAL**, or **BLOCKED**. Include the configured provider/server identity (without secrets), repository and branch, initial and final HEADs, changed paths, commit/state evidence, ackOS verification/commit result, checks actually run, and limitations. Never claim end-to-end success based only on a successful file edit, unit test, proposed patch, or ordinary GitHub write.

## Security note

This skill is model-facing workflow guidance, not an enforcement boundary. The executable ackOS kernel and provider-backed integration must enforce authorization and own execution and verification. If that integration is not actually connected, prepare a proposal and report the blocker; do not perform the side effect directly.
