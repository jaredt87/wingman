# Wingman shared instructions

Read this file first when working in Wingman or a sibling repository that
contains a Wingman pointer.

## Scope and sources

- Read `team.yaml`, `constitution.md`, and the relevant file under
  `brain/context/` before making a change.
- A repository's own `AGENTS.md`, contributor guide, security policy, CI, and
  architecture docs remain authoritative for that repository. Follow both
  local guidance and this shared layer; when they conflict, stop and ask.
- Treat `brain/questions.md` as unresolved. Do not turn a proposed default into
  a claim about the user's actual organization or controls.

## Working rules

- Keep changes scoped to the requested repository and task. Inspect status and
  existing diffs before editing; preserve unrelated work.
- Explain the plan briefly for multi-file or infrastructure changes. Prefer a
  small, reviewable change and update the owning repository's documentation.
- Never expose, request, or commit secrets or customer-sensitive data.
- Do not run `terraform apply`, production deployment, destructive cloud
  actions, migrations, or IAM changes without explicit human approval for the
  specific action. Plans and read-only inspection are preferred first.
- Do not bypass repository CI, review, policy checks, or confirmation gates.
- Do not push, merge, release, or rewrite shared history unless the user
  explicitly requests that exact action.
- Verify changes using the owning repository's documented checks. Report what
  was run and any checks that were not run.
- When a requested state change is designated to run through ackOS, read
  the skill at the Wingman repository root:
  `<Wingman-root>/skills/ackos-control/SKILL.md`. Resolve this path against
  Wingman's root even when working from a sibling checkout; do not resolve it
  against the current working directory. Use only a real, configured,
  provider-backed `ackos_control` integration. The skill, this GitHub
  connection, and the synthetic ackOS demo are not execution authority.
  If the real integration or its supported observation/input path is missing,
  stop before the mutation and report the blocker; never bypass ackOS with
  another write path.

## Keeping the brain useful

- Keep entries short, sourced, and dated when they can go stale.
- Point to existing repository documentation instead of copying it here.
- Route changes to this brain through a pull request when practical; record
  unresolved questions with an owner role and priority.


## Open-source use and licensing

- Wingman is licensed under Apache License 2.0. Review the repository's `LICENSE`; this guidance does not modify the license.
- Before adopting Wingman in another organization, inspect and customize `team.yaml`, `brain/`, and any other context files. Do not assume the example context accurately describes your organization.
- Treat all context and instructions as guidance, not technical enforcement. Configure actual credential permissions, repository protections, CI, and approval gates in the systems that enforce them.
- Keep contributions generalizable and free of secrets, customer-sensitive data, and private organizational context. Prefer links/pointers to authoritative sources rather than embedding sensitive material.
- Follow the target repository's own license, instructions, security policies, and contribution/review rules. This file does not override them.


## ackOS Ecosystem Routing

This repository is part of the ackOS ecosystem:

- **ackOS** — https://github.com/jaredt87/ackOS: the execution-control kernel. Owns authorization, governed execution, independent verification, recovery, and commitment.
- **ackos-api** — https://github.com/jaredt87/ackos-api: the authenticated HTTP interface to ackOS. Delegates execution and verification to ackOS.
- **Wingman** — https://github.com/jaredt87/wingman: shared agent context, instructions, skills, and integration workflows.

### Related repository instructions

Consult the other repositories' agent instructions when a task crosses repository boundaries, changes an integration contract, modifies shared agent workflows, or depends on another component's behavior:

- ackOS instructions: https://github.com/jaredt87/ackOS/blob/main/AGENTS.md
- ackos-api instructions: https://github.com/jaredt87/ackos-api/blob/main/AGENTS.md
- Wingman instructions: https://github.com/jaredt87/wingman/blob/main/AGENTS.md

### Cross-repository coordination

- Read the local instructions of every repository affected by a cross-repository task.
- ackOS remains the execution and control authority; do not create parallel authorization, execution, verification, recovery, or commitment paths.
- ackos-api is an interface and adapter, not a competing control engine.
- Wingman supplies shared agent context and workflows; it must not bypass ackOS for changes designated to be governed through ackOS.
- Identify contract/dependency changes explicitly. Keep changes independently reviewable where practical.
- Verify each affected repository using its own documented checks and report incomplete work, assumptions, and dependencies accurately.

This routing section is an ecosystem navigation and coordination layer. It does not override repository-specific architecture, security, development, or agent instructions. If instructions conflict, stop and resolve the conflict.


## Fractal library routing

Fractal is the ecosystem's knowledge library; Wingman is the experienced librarian and institutional-memory interface over it. Use this relationship for knowledge retrieval, synthesis, source tracing, and proposal preparation—not as an authority chain.

- Fractal Core: https://github.com/jaredt87/fractal-agentic-ecosystem — canonical knowledge-record contracts and local record store.
- Hub Catalog: https://github.com/jaredt87/fractal-hub-catalog — curated capability and blueprint collection.
- Reference Assistant: https://github.com/jaredt87/fractal-assistant — example agent-facing workflow and non-executable policy preview.
- Wingman: this repository — context, retrieval guidance, curation, synthesis, and workflows.

For Fractal-library work, read `skills/fractal-library/SKILL.md` and `brain/context/fractal-library.md`. The Fractal CLI requires an explicit local store root; its initial search is substring-based, not semantic. If the local store is absent or empty, inspect the source repositories directly and do not claim that the library is complete.

Fractal and Wingman do not grant operational authority. For mutations designated to run through ackOS, the existing `skills/ackos-control/SKILL.md` remains mandatory. Do not replace, bypass, or duplicate ackOS authorization, execution, verification, recovery, or commitment.
