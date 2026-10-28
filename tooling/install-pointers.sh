#!/usr/bin/env bash
set -euo pipefail

# Add a short Wingman pointer to the known sibling repositories. Existing
# repository instructions are preserved and receive an appended section once.
wingman_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repos_root="${1:-$(dirname "$wingman_root")}"
marker="<!-- wingman-shared-brain -->"

pointer_content=$(cat <<'EOF'
<!-- wingman-shared-brain -->
## Wingman shared guidance

If the sibling checkout exists, read `../wingman/AGENTS.md` and the relevant
`../wingman/brain/context/` note before starting. This is shared supplemental
guidance; this repository's local instructions, security docs, and CI remain
authoritative. If the sibling checkout is absent, follow this repository's
local guidance and do not assume the Wingman files are available.
EOF
)

repos=(
  ackOS ackOS-main autonomous-control-kernel fractal-agentic-ecosystem
  fractal-assistant fractal-hub-catalog jaredt87 resume
)

for repo in "${repos[@]}"; do
  target="$repos_root/$repo/AGENTS.md"
  if [[ ! -d "$repos_root/$repo" ]]; then
    printf 'SKIP missing repo: %s\n' "$repo"
    continue
  fi
  if [[ -f "$target" ]]; then
    if grep -Fq "$marker" "$target"; then
      printf 'OK already installed: %s\n' "$repo"
    else
      printf '\n%s\n' "$pointer_content" >> "$target"
      printf 'APPENDED: %s\n' "$target"
    fi
  else
    printf '%s\n' "$pointer_content" > "$target"
    printf 'CREATED: %s\n' "$target"
  fi
done
