# Guardrail table

These are conservative proposed defaults because the intake did not establish
the actual credentials or enforcement mechanisms. Review `team.yaml` and
`brain/questions.md` before treating them as policy.

| Action | Block, ask, or allow | Enforced by | Why |
|---|---|---|---|
| Read repo files and run documented local checks | Allow | Filesystem/credential scope; local repo instructions | Routine development work. |
| Read-only cloud inspection or Terraform plan | Ask first until credentials and scope are confirmed; then allow within scope | Cloud IAM and provider credentials; currently unknown | A plan can still expose sensitive configuration. |
| Terraform apply, production deploy, or any cloud write | Ask first for each specific action | Human approval plus cloud/deployment permissions; actual gates unknown | Changes may affect live systems or incur cost. |
| IAM, secrets, migrations, traffic changes, destructive cloud operations | Block by default; require explicit human-led procedure | IAM, deployment controls, and approvals; actual gates unknown | High impact and difficult to reverse. |
| Read, copy, or commit secrets or customer-sensitive records | Block | Secret handling and credential design; currently unknown | Keep sensitive material out of prompts, logs, and Git. |
| Skip CI, reviews, branch protection, dry-run, or confirmation gates | Block | Repository protections and CI where configured; instruction only otherwise | Existing controls must remain effective. |
| Push, merge, release, rewrite shared history, or write to external systems | Ask first for the exact destination and action | Git hosting or application permission; currently unknown | Publishing changes has external effects. |
