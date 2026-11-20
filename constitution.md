# Wingman constitution

These are the initial shared rules. The enforcement column distinguishes
technical controls from instructions; prose alone cannot restrict credentials
or stop a command.

| Rule | What enforces it |
|---|---|
| Follow the target repository's own instructions, security policy, and CI. | Repository controls where configured; otherwise instruction only. |
| Do not expose or commit secrets or customer-sensitive data. | Credentials and secret scanning where configured; instruction only otherwise. |
| Get action-specific human approval before production, destructive, IAM, migration, or cloud-write actions. | Cloud credentials and deployment gates should enforce this; actual controls are an open question. Until confirmed, instruction only. |
| Never bypass review, CI, policy, or confirmation gates. | CI/repository protections where configured; instruction only otherwise. |
| Verify the change using the repository's documented checks and report the evidence. | CI where configured; instruction only for local verification/reporting. |
| Keep the shared brain short, sourced, and reviewable; point to local sources rather than copy them. | Review process and maintenance cadence are unconfirmed; instruction only until approved. |
