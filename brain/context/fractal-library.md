# Fractal Library Context

**Mental model:** Fractal is the library; Wingman is the experienced librarian.

Wingman provides retrieval guidance, institutional memory, source tracing, curation, and synthesis over Fractal's knowledge architecture. It should help agents understand what is known, where it came from, how it relates to other information, and what remains uncertain. It should not become a second wiki that copies every source repository.

## Repositories

- Fractal Core: https://github.com/jaredt87/fractal-agentic-ecosystem
  - Owns canonical knowledge-record contracts and the first local record store.
  - Initial record types: `KnowledgeObject`, `EvidenceRecord`, and `KnowledgeRelationship`.
  - CLI: `python -m knowledge_layer.cli --store-root <explicit-path> <command>`.
- Hub Catalog: https://github.com/jaredt87/fractal-hub-catalog
  - Curates capability descriptors, blueprint definitions, and catalog lifecycle evidence.
  - Catalog admission is not runtime authorization.
- Reference Assistant: https://github.com/jaredt87/fractal-assistant
  - Demonstrates a small pipeline and non-executable policy preview.
  - Mock executor; no real external side effects.
- Wingman: https://github.com/jaredt87/wingman
  - Maintains shared context, source pointers, librarian workflows, and institutional memory.

## Knowledge and authority boundaries

Knowledge, evidence, provenance, capability descriptions, proposals, authorization, and execution are distinct.

- Fractal organizes knowledge and records evidence; it does not establish truth merely by storing a record.
- A source reference, digest, publisher name, or signature establishes only its specific property; none should be treated as a universal trust signal.
- A Hub Catalog entry or accepted catalog state is not permission to invoke a tool.
- A proposal is not authorization.
- Operational authorization comes from external governance and is enforced at the execution boundary.
- MCP is an interoperability surface, not the architecture or an authority system.
- No agent-facing Fractal surface should expose a generic execute operation.

For currently ackOS-governed mutations, ackOS remains the execution-control authority. The Fractal knowledge workflow must not create a competing execution or authorization path. The relationship between future Xavier/Recon concepts and ackOS must be resolved explicitly before execution integration is built.

## Current Fractal knowledge model

The first Fractal knowledge increment is merged into Core `main` in [PR #39](https://github.com/jaredt87/fractal-agentic-ecosystem/pull/39) (merge commit [`6c75f09`](https://github.com/jaredt87/fractal-agentic-ecosystem/commit/6c75f09405d1966542873987a500aef8725e1ff6)).

It includes:
- `KnowledgeObject`: a concept, system, capability, decision, document, proposal, or resource.
- `EvidenceRecord`: a source-backed claim about a subject, with capture time and optional digest/freshness boundary. Assessments are attributed opinions, not cryptographic verification.
- `KnowledgeRelationship`: a typed link between records, optionally citing evidence records.
- `RecordStore`: explicit-root, local, append-only JSON persistence; identical writes are idempotent, different content under an existing ID is rejected.
- CLI: `validate`, `put`, `get`, `list`, `search`, `evidence`, `relationships`, and `check`.

The source-linked starter collection is in `examples/knowledge/seed/` in Fractal Core. It contains 11 records: four knowledge objects, four deliberately unassessed evidence records, and three typed relationships. Its evidence is pinned to source revisions; do not infer that the evidence has been independently verified.

The initial search is case-insensitive substring matching, not semantic retrieval. The explicit `check` command reports dangling subject, relationship endpoint, and evidence references, but does not establish that evidence supports a claim. The store does not fetch sources, verify provenance, authenticate identities, replicate, or authorize actions.

The default example store path `.state/library` is local data and is ignored by Git. Do not commit private or user-specific library contents. Use an explicit store root and follow the target Fractal repository's instructions.

## First local librarian workflow

From a Fractal Core checkout, inspect the current instructions and load the checked-in starter collection into a local store when appropriate:

```bash
for file in examples/knowledge/seed/*.json; do
  python -m knowledge_layer.cli --store-root .state/library put "$file"
done

python -m knowledge_layer.cli --store-root .state/library check
python -m knowledge_layer.cli --store-root .state/library search "Wingman"
```

Then follow returned record IDs to their evidence and relationships, and inspect the authoritative source files directly. The store is a retrieval aid, not proof that a claim is true or that all relevant knowledge has been found. Do not describe substring search as semantic or exhaustive.

When answering:
- Cite or link the source repository/file, not only the library record.
- Distinguish direct source facts from evidence records, prior assessments, and Wingman's synthesis.
- Surface conflicting evidence, stale `freshUntil` boundaries, missing digests, and unresolved references.
- Explain what is not known when evidence is incomplete.
- Do not elevate an assessment of `supports` into cryptographic verification or certainty.

## Curation and proposals

Only add records when the user explicitly asks to save, record, or curate the information in the Fractal library, or has otherwise approved that specific curation.

Use stable, unique record IDs. IDs are immutable in the initial store. For a revision, create a new ID and add a `supersedes` relationship; never overwrite an existing ID. Record actual source URIs and capture times. Include a SHA-256 digest only when the exact source bytes were actually hashed. Keep evidence unassessed unless an identifiable reviewer actually assessed it.

When research suggests a change, prepare a proposal that references relevant knowledge and evidence record IDs. State the requested transition, target resource, before-state evidence, desired outcome, uncertainty, and risks. Keep the proposal separate from the source records and never treat it as authorization. Route protected state changes through the applicable external governance and execution-control system.

Never store secrets, credentials, or customer-sensitive data in the knowledge library.

## Source-of-truth pointers

Prefer current files on Core `main` over copied descriptions:
- [Fractal architecture thesis](https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/architecture-thesis.md)
- [Knowledge record model](https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/knowledge-record-model-v1alpha1.md)
- [Knowledge record store](https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/knowledge-record-store.md)
- [Knowledge CLI](https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/knowledge-library-cli.md)
- [Canonical shared ecosystem context](https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/AGENT_CONTEXT.md)

The Core repository's `AGENTS.md` and the Wingman `skills/fractal-library/SKILL.md` define the operating instructions. Check the target branch and repository state before relying on any implementation detail.
