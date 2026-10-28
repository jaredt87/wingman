# Shared review checklist

- Is the change in the correct repository and within the requested scope?
- Did it preserve local instructions, security boundaries, and existing work?
- Are assumptions identified, and are unresolved policy questions still open?
- For infrastructure, does the diff/plan show the intended resources and no
  unapproved destructive, IAM, or production change?
- Did the owning repository's documented CI and verification commands run?
- Are docs updated in their source repository, without copying them into
  Wingman unnecessarily?
- Are secrets and sensitive values absent from the change and its output?
- Does the summary state checks run, checks skipped, and any human action needed?
