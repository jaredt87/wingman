---
name: go-change
description: Use when making a scoped change in a Go repository covered by Wingman.
---

# Go change

1. Read the repository's own `AGENTS.md`, README, security guidance, and CI.
2. Inspect status and the relevant code before editing; preserve unrelated work.
3. Make the smallest coherent change and update the owning repository's docs
   where needed.
4. Run that repository's documented format, vet, and test checks. Do not claim
   a check passed unless it ran successfully.
5. Report the change and verification. Do not push, merge, release, or rewrite
   history unless the user explicitly asked for that action.
