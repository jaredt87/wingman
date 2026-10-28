# Skills

The repeated request types are still being learned during the pilot; revise
candidate skills as real usage provides evidence.

- `ackos-control`: route designated state-changing work through a real,
  provider-backed ackOS integration; fail closed if the integration is absent.
  Like every skill here, this is workflow guidance, not a security boundary.
- `terraform-plan-review`: review a saved plan for scope, destructive changes,
  IAM, and production risk; never apply it.
- `go-change`: orient in a Go repo, make a scoped change, and run that repo's
  required checks; never bypass its invariants or publish without approval.
- `repo-onboarding`: summarize a repo's purpose, local instructions, CI, and
  unresolved setup questions; never claim undocumented controls exist.
