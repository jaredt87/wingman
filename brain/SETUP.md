# Initial setup plan

## First week

1. Review `team.yaml` and resolve P1 questions about the Terraform repo,
   environments, production path, and agent credentials.
2. Pilot the shared entry point and repo pointers on `ackOS-main` for two weeks.
   Compare its instructions with `AGENTS.md` and CI; report conflicts before
   changing either source.
3. Use the `repo-onboarding` and `go-change` candidate skills on ordinary,
   non-production tasks. Try `terraform-plan-review` only on a saved plan and
   never apply it.
4. Record whether the pointers load in the terminal agent, IDE assistant, and
   desktop chat you use; revise the entry points based on actual behavior.

## Second week

5. Ask whether the pilot reduced repeated explanations or missed local checks;
   replace inferred skills with the actual top request types.
6. Confirm sensitive-data rules, approval gates, and what “done” means before
   describing them as settled policy.
7. Review pointer coverage and stale repository notes. Keep updates in each
   repository's owning change review; Wingman does not replace those reviews.

## Access and approvals

- No connector or cloud access request is identified yet. Prefer no credentials
  or read-only credentials for the pilot.
- A human must approve any production write, Terraform apply, IAM change,
  destructive operation, merge, release, or external publication.
- Actual production approver, cloud identity, and repository review rules are
  open questions. Do not request or store credential values in Wingman.
