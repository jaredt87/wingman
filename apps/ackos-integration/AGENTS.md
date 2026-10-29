# ackOS integration workspace instructions

This directory is the app-specific entry point for the Wingman → ackOS integration. It is instructions and configuration documentation, not an executable agent runtime.

## Load shared context first

Before changing anything, read these sources from the Wingman repository root:

1. [Shared instructions](../../AGENTS.md)
2. [Team context and open questions](../../team.yaml)
3. [Wingman constitution](../../constitution.md)
4. [ackOS repository pointer](../../brain/context/ackOS-main.md)
5. [Canonical ackOS control skill](../../skills/ackos-control/SKILL.md)

The linked skill is authoritative for this workflow. Do not copy it into this directory or weaken its requirements. Also follow the target repository's own instructions, security guidance, review process, and checks.

## Intended architecture

`Wingman coordinator → host MCP runtime → ackOS `cmd/ackos-mcp-api` (stdio) → authenticated ackos-api → ackOS kernel/provider → allowlisted repository checkout`

The production adapter is already implemented in ackOS. Do not recreate it or use the synthetic `cmd/ackos-mcp` demo as execution authority. ackos-api/ackOS own authorization, execution, independent verification, recovery, and commitment; this workspace is only the client-side context.

## Protected mutations

- A protected mutation may proceed only through the actual callable, provider-backed `ackos_control` MCP tool exposed by the host's real tool registry.
- Use the adapter's supported tool schema and server-owned observation flow. Never invent repository IDs, observations, fingerprints, opaque observation tokens, or concurrency values. The adapter obtains a fresh observation and forwards its opaque token unchanged.
- Treat authentication failures, stale observations, malformed responses, timeouts, and ambiguous outcomes as failures. Do not retry with stale values.
- Require explicit ackOS confirmation of independent verification and commitment, then independently inspect the resulting provider state when a supported read path is available.
- Never substitute direct HTTP mutation, ordinary file edits, Git writes, GitHub write APIs, a mock, or the synthetic demo.
- Never modify the Terraform test target, push, merge, provision infrastructure, or run `terraform apply` as part of establishing the MCP connection.

## Runtime registration and secrets

The host-specific MCP registration is intentionally not specified in this repository yet: the execution host and its supported project-local configuration mechanism have not been established in this session. Do not assume a `.mcp.json`, Codex config, Claude Code config, or other file is consumed by the real host. Do not claim this workspace connects the runtime by itself.

Follow [ackOS's production adapter instructions](https://github.com/jaredt87/ackOS/blob/main/integrations/mcp/HTTP_API_ADAPTER.md) when configuring the host. The adapter entry point is `cmd/ackos-mcp-api`, launched from the ackOS repository root using MCP over stdio (documented command: `go run ./cmd/ackos-mcp-api -api-timeout=10s`). Supply `ACKOS_API_URL` and `ACKOS_API_BEARER_TOKEN` through the host's supported secure environment/secret mechanism. The URL must use HTTPS except for loopback test servers. Never commit or print credentials, and do not invent an API origin.

Before declaring the connection ready, record evidence separately for: workspace instructions loaded; adapter process started; MCP handshake succeeded; the real host registry exposes `ackos_control` with the expected schema; and an authenticated, non-mutating API connection succeeded. A config entry, unit test, or mock server alone proves none of the latter runtime facts.

## Required outcome report

Use exactly one overall status:

- **PASS** — the workspace is usable and the real host has discovered the production adapter's callable `ackos_control` tool.
- **PARTIAL** — workspace/code work is complete, but an identified external configuration or service blocks full validation.
- **BLOCKED** — host or required access is unavailable, so the real connection cannot be demonstrated.

List evidence for each step actually completed, tests actually run, remaining access/configuration needs, and whether the later Terraform integration test is ready. Do not claim the Terraform end-to-end test passed during runtime setup.
