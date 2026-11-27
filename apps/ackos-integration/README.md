# Wingman ackOS integration workspace

This app-specific workspace gathers only the context and setup requirements for the Wingman → ackOS integration. It does not implement a second agent runtime or duplicate the production adapter.

## Start here

1. Read [this workspace's instructions](AGENTS.md).
2. Load the shared Wingman entry point and policy sources listed there.
3. Reuse the canonical [`ackos-control` skill](../../skills/ackos-control/SKILL.md); do not fork its policy.
4. Follow the target repository's own `AGENTS.md`, security guidance, review loop, and required checks.

## Intended runtime

```text
Wingman context + coordinator
        ↓
actual host MCP runtime / callable tool registry
        ↓  MCP over stdio
ackOS cmd/ackos-mcp-api
        ↓  authenticated HTTPS
ackos-api → ackOS kernel/provider → allowlisted disposable repository
```

The production adapter and its documented schema are maintained in [ackOS](https://github.com/jaredt87/ackOS/blob/main/integrations/mcp/HTTP_API_ADAPTER.md). It exposes `ackos_control` with `repository_id`, `branch`, `path`, `mode`, and `content_base64`. The adapter obtains the provider observation and passes its opaque token through to ackos-api; callers must not manufacture those values.

## Host configuration status

**Not configured in this repository.** The current ChatGPT-hosted session exposes a GitHub connector, but it does not expose a project-local MCP configuration surface, local process launcher, or the host's underlying callable-tool registry for registering an arbitrary stdio process. Therefore, adding a guessed configuration file here would not establish a real connection.

Once the intended execution host is available, register the existing adapter using that host's documented project/workspace mechanism. The adapter command, when launched with the ackOS checkout as its working directory, is:

```sh
go run ./cmd/ackos-mcp-api -api-timeout=10s
```

Provide these environment variables through the host's secure secret/environment facility, not this repository:

- `ACKOS_API_URL` — configured ackos-api origin; HTTPS is required except for loopback tests.
- `ACKOS_API_BEARER_TOKEN` — bearer credential.

Do not substitute a placeholder URL as a real endpoint, commit credentials, or expose them in logs. The API service itself must be configured independently with its repository allowlist and signing secret as documented in ackos-api. A working adapter process is not proof that authentication or tool discovery succeeded.

## Read-only readiness gate

Before any mutation, demonstrate all of the following against the actual host and production adapter:

- [ ] This workspace's instructions and the canonical safety skill are loaded.
- [ ] The production `ackos-mcp-api` process starts and the MCP handshake succeeds.
- [ ] The actual host registry lists callable `ackos_control` and its schema matches the production adapter.
- [ ] A real authenticated, non-mutating API connection succeeds without exposing the bearer token.
- [ ] Startup, authentication, schema, and invocation failures remain failures; no alternate mutation route is used.

Do not modify the Terraform target or run `terraform apply` while completing this gate. The eventual end-to-end test is a separate task and is not ready until the live tool connection is demonstrated.
