---
name: terraform-plan-review
description: Use when asked to inspect or explain a Terraform plan before a human approves infrastructure changes.
---

# Terraform plan review

1. Read the target repository's instructions and identify the exact workspace,
   environment, and plan artifact. Do not ask the user to paste credentials.
2. Inspect the plan as data. Summarize creates, updates, deletes, replacements,
   IAM changes, public exposure, and sensitive values without reproducing
   secrets.
3. Compare the plan with the stated request. Call out unexplained drift or
   actions outside scope.
4. State uncertainties and the required human approver. Do not run `apply`,
   approve, or deploy. A plan review is advisory and does not prove a change is
   safe.
5. Produce a concise review with risk findings and questions.
