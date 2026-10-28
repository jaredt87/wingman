# Shared workflow

1. Identify the target repository and read its local agent/contributor/security
   guidance, CI configuration, and relevant architecture docs.
2. Read its context note under `brain/context/`. Treat notes as pointers, not
   replacements for the source documents.
3. Inspect the working tree and the exact task scope. Preserve unrelated work.
4. For consequential or multi-file work, state a short plan. Ask before
   production writes, destructive actions, IAM changes, migrations, external
   publishing, or other actions listed in `team.yaml`.
5. Make the smallest coherent change. Keep local decisions in the owning repo.
6. Run the owning repo's documented checks; do not invent a successful result
   if a check could not run.
7. Summarize the changes, evidence, remaining risks, and unresolved questions.

Unknown practices remain open until the primary maintainer confirms them.
