# ackOS-main

- **Role:** active Go kernel checkout (separate local checkout from `ackOS`).
- **Start with:** root `AGENTS.md`; it defines project boundaries, required
  checks, forbidden changes, and review conventions. Also read `SECURITY.md`,
  `docs/ARCHITECTURE.md`, and `docs/RESEARCH_BOUNDARIES.md` when relevant.
- **CI:** `.github/workflows/ci.yml` validates agent integration manifests and
  skill metadata, then runs gofmt, `go vet ./...`, `go test ./...`, and
  `go test -race ./...`.
- **Local state note:** this checkout may be on a feature branch. Preserve its
  branch and existing SDD files; inspect `git status` before editing.
