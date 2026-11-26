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

The first Fractal knowledge increment includes:
- `KnowledgeObject`: a concept, system, capability, decision, document, proposal, or resource.
- `EvidenceRecord`: a source-backed claim about a subject, with capture time and optional digest/freshness boundary. Assessments are attributed opinions, not cryptographic verification.
- `KnowledgeRelationship`: a typed link between records, optionally citing evidence records.
- `RecordStore`: explicit-root, local, append-only JSON persistence; identical writes are idempotent, different content under an existing ID is rejected.
- CLI: `validate`, `put`, `get`, `list`, `search`, `evidence`, `relationships`, and `check`.

The initial search is case-insensitive substring matching. It is not semantic retrieval. The explicit `check` command reports dangling subject, relationship endpoint, and evidence references, but does not establish that evidence supports a claim. The store does not fetch sources, verify provenance, authenticate identities, replicate, or authorize actions.

The default example store path `.state/library` is local data and is ignored by Git. Do not commit private or user-specific library contents. Use an explicit store root and follow the target Fractal repository's instructions.

## Integration dependency

The Fractal Core knowledge-record schema, store, and CLI are being introduced in [Fractal Core PR #39](https://github.com/jaredt87/fractal-agentic-ecosystem/pull/39). Merge that foundation before treating the CLI workflow as available on the default branch. The source links below use the implementation branch until the change lands.

## Source-of-truth pointers

Prefer links to current repository files over copying them into Wingman:
- Fractal architecture thesis: https://github.com/jaredt87/fractal-agentic-ecosystem/blob/architecture/library-model-foundation/docs/architecture-thesis.md
- Knowledge record model: https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/knowledge-record-model-v1alpha1.md
- Knowledge record store: https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/knowledge-record-store.md
- Knowledge CLI: https://github.com/jaredt87/fractal-agentic-ecosystem/blob/main/docs/knowledge-library-cli.md
- Shared ecosystem context: https://github.com/jaredt87/fractal-agentic-ecosystem/blob/architecture/library-model-foundation/AGENT_CONTEXT.md

This context is a pointer and operating guide, not proof that the referenced implementation is available in every local workspace. Check the target branch and repository state before relying on it.
