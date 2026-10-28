# ackOS

- **Role:** canonical executable ACK control kernel and agent integrations.
- **Stack:** Go 1.25; Claude, Gemini, and ChatGPT-facing integration files.
- **Start with:** `README.md`, `SECURITY.md`, `docs/ARCHITECTURE.md`,
  `docs/RESEARCH_BOUNDARIES.md`, `GEMINI.md`, and `skills/` or integration
  guidance relevant to the change.
- **CI:** `.github/workflows/ci.yml` validates integration manifests and skill
  frontmatter, then runs gofmt, `go vet ./...`, `go test ./...`, and
  `go test -race ./...`.
- **Local checkout note:** at intake this checkout was 124 commits behind
  `origin/main` and contained an unrelated untracked `ackos-mcp` directory.
  Inspect status and synchronize deliberately before work; preserve that
  directory.
