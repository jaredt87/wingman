# Wingman

**Shared agent context, instructions, and skills for repository-based work.**

Wingman is a shared-context repository intended to help AI agents and developers work consistently across repositories. It provides reusable instructions, team context, skills, guardrails, and pointers to repository-specific documentation. Wingman is not a standalone application or agent runtime; it is consumed by compatible agent hosts and workflows.

## Getting started

1. Clone this repository and review its contents before using or distributing its context.
2. Read `AGENTS.md`, `team.yaml`, and `constitution.md`.
3. Review the relevant files under `brain/context/` for the work you're doing, and treat `brain/questions.md` as unresolved context rather than established facts.
4. Follow the target repository's own `AGENTS.md`, security policy, documentation, and CI requirements. Local repository guidance remains authoritative for that repository.
5. For Fractal knowledge retrieval and curation, follow `skills/fractal-library/SKILL.md`. Fractal is the library; Wingman is the librarian. This workflow does not grant authority.
6. For changes that must be governed by ackOS, follow `skills/ackos-control/SKILL.md`. It requires a real, callable, provider-backed ackOS integration; instructions alone do not enforce authorization.

## Repository structure

- `AGENTS.md` — shared agent working rules and pointers.
- `team.yaml` — working context and configuration (review and customize before adopting).
- `constitution.md` — shared principles and guardrails.
- `brain/` — contextual knowledge, pointers, and unresolved questions.
- `skills/` — task-specific workflows, including `fractal-library/` for knowledge retrieval and `ackos-control/` for governed mutations.
- `brain/context/fractal-library.md` — pointers and operating context for Fractal Core, Hub Catalog, and the reference Assistant.

Contents are intentionally lightweight and should point to authoritative sources instead of duplicating them. Review contextual files for privacy, accuracy, and applicability before using them in another organization.

## Safety and limitations

Wingman provides model-facing instructions and context. These instructions are not a security boundary and cannot themselves restrict credentials, commands, or access. Configure permissions, credential scopes, repository protections, CI, and deployment gates in the systems that enforce them. Require action-specific human approval for consequential operations as described by the applicable policies.

Do not treat example or unresolved context as facts about your organization. Adapt the repository to your environment and inspect all context files before adopting them.

## License

Wingman is licensed under the Apache License 2.0. See [LICENSE](LICENSE).

Copyright 2026 Jared Thomson.
