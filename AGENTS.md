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
