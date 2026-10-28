# Team brain intake prompt

Paste everything below the line into an AI assistant (Claude Code, Claude Desktop, Cursor, or similar) at the start of setting up a team brain repo. It interviews the person setting it up, then produces the team metadata and a setup plan tailored to how the team will actually use it.

It is deliberately generic: it works for software, platform, cloud, SRE, data, security or IT teams, and it never asks for names, secrets or anything that identifies a person or system beyond what the team chooses to write.

---

You are helping me set up a **team brain**: a git repository of shared instructions, rules, knowledge and reusable skills that every AI coding agent and every new teammate loads before working in our repos. Your job right now is to **interview me**, then produce the team's metadata and a setup plan. Don't write any other files yet.

## How to run the interview

- Go in **rounds**, one round per message, 3–6 questions each. Wait for my answers before the next round.
- For every question, offer a **sensible default** in brackets so I can answer "default". Mark which questions are **required** and which are optional.
- Adapt as you go: skip questions my earlier answers made irrelevant, and add follow-ups where an answer opens a risk (production access, regulated data, shared credentials).
- Use **multiple choice** where the answers are predictable, and free text where they aren't.
- **Never ask for or record** secrets, tokens, passwords, account IDs, IP addresses, hostnames, customer data, or people's personal details. If I paste any, tell me, drop it, and use a placeholder like `<prod-account>` or `<on-call-rotation>`.
- Use **roles, not names** for people (`team lead`, `on-call engineer`, `approver for production`).
- If I say "I don't know", record it as an open question with who should answer it, and move on.
- Keep a running summary. At the end of each round, show the metadata collected so far in a short YAML block so I can correct it.

## The rounds

### Round 1 — Purpose and scope (required)
1. What kind of team is this? (software engineering, platform, cloud/infrastructure, SRE/operations, data/analytics, security, IT/systems, other) — more than one is fine.
2. In one sentence, what should the brain help with first? (e.g. safer changes, faster onboarding, ticket quality, incident investigation, consistent reviews)
3. Who is it for? (only this team / this team plus requesting teams / new hires first / eventually other teams too)
4. What would make you call it a success in 90 days? Give 1–3 measurable signs.
5. What must it never become? (e.g. a second wiki nobody updates, extra paperwork, an agent with production write access)

### Round 2 — The people using it (required)
1. Team size, and the rough mix of roles and seniority.
2. Time zones and whether there's an on-call rotation.
3. Which AI tools do people use today, and which will the brain support? (terminal agents, IDE assistants, desktop chat, browser chat, none yet)
4. Operating systems and shells people work in.
5. How comfortable is the team with AI agents running commands? (suggest only / run read-only commands / run commands with approval / mostly autonomous in dev)
6. Who will maintain the brain, and how much time do they have for it?

### Round 3 — What the team works on (required)
1. List the repositories or systems the team touches, grouped by how often: daily, weekly, rarely. Use generic names if you prefer (`app-backend`, `infra-live`, `config-management`).
2. Main languages, frameworks and tools. For infrastructure teams: IaC tools, configuration management, orchestration, cloud providers.
3. Environments (e.g. dev, stage, production) and how a change gets from a branch to production.
4. CI/CD system and what it checks today.
5. Which of these repos already have their own contributor guides, governance docs, agent instructions or reusable scripts? (The brain should point to those, not copy them.)

### Round 4 — How work flows (required)
1. Where requests arrive (ticket tracker, chat channel, form, email) and how they become work items.
2. What a good ticket or task looks like here, and what "done" means: merged, deployed, or verified?
3. Code review norms: who reviews, what they look for, how many approvals.
4. Branching and release practice.
5. How decisions get recorded today, if at all (decision records, wiki pages, chat threads).
6. The most common repeated request types (top 3–5). These are candidates for the first skills.

### Round 5 — Knowledge sources
1. Where documentation lives (wiki, docs repo, READMEs) and how current it is.
2. Runbooks and incident history: where, and what format.
3. Which chat channels matter and what each is for.
4. Which sources could an agent read **read-only** through a connector? (tracker, wiki, chat, cloud provider, observability, source host)
5. What is commonly explained twice? Those become the first memory entries.

### Round 6 — Risk and guardrails (required)
1. What must an agent **never** do? Suggest a starting list for my team type, for example:
   - software: push to main, merge, release, change production config, run migrations;
   - platform/cloud: apply infrastructure changes, run config management for real, change IAM, toggle production traffic;
   - data: read production rows, export data, change pipelines in production;
   - security: change policies, rotate or read secrets, disable controls.
2. Which actions should **ask a human first** instead of being blocked? (e.g. writing to the ticket tracker, destructive git commands)
3. What credentials will agent sessions use? Is a read-only role available? (The real boundary is the credential, not the instructions.)
4. Any regulated or sensitive data (customer PII, payments, health, financial)? Rules for keeping it out of prompts.
5. Who approves production changes, and where (pull request, deployment tool, change board)?
6. Which safety gates exist today that must never be bypassed (dry-run flags, confirmations, approvals)?

### Round 7 — Keeping it current
1. What facts go stale fastest (inventory, versions, owners, on-call, endpoints)? Could any be refreshed automatically from a read-only source on a schedule?
2. How should changes to the brain be reviewed? (pull requests to the brain repo, owners per section)
3. How often should someone review whether the team's practices are still current? (default: a light monthly check, a deeper quarterly review)
4. How should lessons from incidents and investigations get back into the brain?

### Round 8 — Distribution and rollout
1. How will people load the brain? (a plugin or extension, pointer files in each repo, a global instruction file per tool)
2. Pilot plan: who tries it first, on what kind of real work, for how long?
3. Will other teams adopt it later? If so, what's shared core and what's per-team?
4. Where should the human-readable version live (wiki, docs site), and is that a copy generated from the repo?

## What to produce after the last round

Produce these, in this order, each in its own code block or section:

### 1. `team.yaml` — the team metadata

Use this shape. Fill what I answered, leave `null` and add an `open_questions` entry for what I didn't. Keep every value generic and free of secrets.

```yaml
team:
  name: <team-slug>
  type: [platform]            # software | platform | cloud | sre | data | security | it
  purpose: "<one sentence>"
  success_90d: ["<signal>", "<signal>"]
  anti_goals: ["<what it must never become>"]
people:
  size: <n>
  roles: [<role>, <role>]
  time_zones: [<tz>]
  on_call: true | false
  brain_maintainers: [<role>]
tools:
  agents: [<terminal agent>, <ide assistant>, <desktop chat>]
  agent_autonomy: suggest | read_only | run_with_approval | autonomous_in_dev
  platforms: [macos, linux, windows]
work:
  repos:
    daily:  [{name: <repo>, own_governance: true | false}]
    weekly: [{name: <repo>, own_governance: true | false}]
    rarely: [<repo>]
  stack: [<language/tool>]
  environments: [dev, stage, production]
  ci: <system>
  path_to_production: "<branch → review → merge → deploy → verify>"
flow:
  intake: [<tracker>, <channel>]
  done_means: merged | deployed | verified
  review: {approvals: <n>, required_reviewers: [<role>]}
  decisions_recorded_in: <place or null>
  top_request_types: [<type>, <type>, <type>]
knowledge:
  docs: <where>
  runbooks: <where>
  channels: [{purpose: <purpose>}]
  read_only_connectors: [<tracker>, <wiki>, <cloud>]
guardrails:
  never: [<action>]
  ask_first: [<action>]
  agent_credentials: read_only | scoped_write | unknown
  sensitive_data: [<category>]
  production_approval: "<who / where>"
  gates_never_bypassed: [<gate>]
freshness:
  auto_refresh: [{source: <read-only source>, cadence: weekly}]
  brain_changes_via: pull_request
  practice_review: {light: monthly, deep: quarterly}
rollout:
  load_via: [plugin, pointer_files]
  pilot: {who: [<role>], duration_days: <n>}
  multi_team: false
open_questions:
  - {question: "<text>", owner: <role>, priority: P1 | P2 | P3}
```

### 2. Recommended repo layout

A directory tree for the brain repo, tailored to my answers. Include only what this team needs now; mark what to add later. A typical starting point:

```text
AGENTS.md                 # entry point every tool reads first
constitution.md           # the few non-negotiables, and what enforces each
team.yaml                 # the metadata above
brain/
  workflow.md             # how agents work here: modes, when to stop, handoff
  memory/                 # short entries: settled decisions and known traps
  decisions/              # decision records for choices with consequences
  context/                # maps of each repo/system, pointing at its own docs
  standards/              # review checklist, ticket format, per-tool rules
  runbooks/               # procedures a human runs
  questions.md            # open questions with owners and priority
skills/                   # reusable task instructions, one folder per skill
tooling/                  # checks: links, ownership, staleness, guard tests
```

### 3. Constitution draft

5–8 short rules, written for my team type, each with **what enforces it** (credentials, a hook or guard, CI, review, or "instruction only"). Be honest about which rules only rely on instructions.

### 4. First skills to build

The 3 most valuable skills, chosen from my top request types and pain points. For each: name, when it triggers, what it produces, and what it must never do.

### 5. Guardrail table

| Action | Block, ask, or allow | Enforced by | Why |
|---|---|---|---|

### 6. Setup plan

A short, ordered plan for the first two weeks: what to write first, what to automate, who pilots it, and how we'll know it's working. Flag anything that needs an approval or access request.

### 7. Open questions

The `open_questions` list, sorted by priority, each with an owner role.

Before producing the outputs, show me a one-paragraph summary of what you understood and ask: "Anything wrong or missing before I generate the files?"
