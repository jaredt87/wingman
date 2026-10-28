# autonomous-control-kernel

- **Role:** ACK research and formal verification authority; its README says the
  canonical executable kernel is in `ackOS`.
- **Stack:** Go 1.24 and TLA+/TLC, with shell/Python review-gate tooling.
- **Start with:** `README.md`, `docs/REPOSITORY_ROLES.md`,
  `docs/RESEARCH_REPOSITORY_BOUNDARY.md`, and `docs/ACK_SAFETY_CONTRACT.md`.
- **CI:** `verification.yml` runs Go tests/vet, review-gate adversarial checks,
  and a pinned TLC campaign; `review-gate-trusted.yml` enforces its trusted
  review gate. Follow the repository's workflow rather than treating Wingman
  guidance as a substitute.
