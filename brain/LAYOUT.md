# Recommended repo layout

This is the initial layout, limited to the needs identified so far:

```text
AGENTS.md                         # Shared entry point
constitution.md                   # Non-negotiables and enforcement limits
team.yaml                         # Team metadata and open questions
brain/
  workflow.md                     # Shared agent workflow
  questions.md                    # Unresolved questions with owner and priority
  context/                        # Repo maps that point to local sources
  decisions/README.md             # Add records when cross-repo decisions exist
  standards/
    guardrails.md                 # Proposed action policy and actual enforcement
    review-checklist.md
  runbooks/README.md              # Add runbooks only when owners/sources are known
  SETUP.md                        # Two-week pilot and approval needs
  LAYOUT.md                       # This map
skills/                           # Reusable workflows; see skills/README.md
tooling/install-pointers.sh       # Idempotent sibling-repo pointer installer
```

**Add later:** `brain/memory/` after stable repeated lessons emerge; link and
staleness checks under `tooling/` after the context has a dependable source.
No wiki copy, automatic inventory refresh, connector, or per-team layer is
needed until the open questions establish a use for it.
