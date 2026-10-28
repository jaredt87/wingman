# Repository map

These are the eight Git repositories found under `/Users/jt/repos` during
intake. Their local README, CI, and agent-guidance files are the sources of
truth. Repo names and branches can move; recheck before acting.

| Repository | Current role / stack | Guidance and checks |
|---|---|---|
| `ackOS` | Executable Go kernel and agent integrations | `README.md`, `SECURITY.md`, `docs/`, `GEMINI.md`, `skills/`; GitHub Actions Go format/vet/test/race and integration validation. Local checkout is behind its remote and has unrelated untracked `ackos-mcp`; preserve it. |
| `ackOS-main` | Active Go kernel checkout | `AGENTS.md` is detailed and authoritative; also `SECURITY.md`, `docs/`, `GEMINI.md`; CI validates integrations and runs Go format/vet/test/race. |
| `autonomous-control-kernel` | ACK research and formal verification; Go, TLA+/TLC | `README.md`, `docs/REPOSITORY_ROLES.md`, research docs; GitHub Actions Go tests/vet, review-gate adversarial checks, TLC campaign, trusted review gate. |
| `fractal-agentic-ecosystem` | Python demo platform, API, JavaScript UI, YAML governance | `README.md`, `governance/`, `architecture/`, `specifications/`, `docs/agents.md`, `pyproject.toml`; no workflow was found. |
| `fractal-assistant` | Empty starter repository at inspection (`.gitkeep`) | No README, agent guidance, or CI found. |
| `fractal-hub-catalog` | YAML infrastructure blueprint catalog | `README.md`, `catalog.yaml`, `blueprints/`; no workflow or agent guide found. |
| `jaredt87` | Profile repository | `README.md`; a placeholder GitHub Actions workflow exists but has an incomplete setup step. |
| `resume` | Markdown/Jekyll resume site | `README.md`, `docs/`, `_config.yml`; no workflow or agent guide found. |

No Terraform-named repo or Terraform files were found in the inspected tree.
The user said Terraform is normal work, so locate that repo before treating this
inventory as complete. No CI observation establishes whether a deployment
requires approval or what credentials are available.
