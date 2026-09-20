# External Repository Candidates — 2026-09-20

Status: EVALUATED / NON-CANONICAL / NO EXTERNAL REPOSITORY ADMITTED AS EVIDENCE

Base Testament head:
- repository: thebrazenbeard/testament
- branch: foundation/testament-v1
- commit: 3ff338187d716a56e39ffdc4780cd6d4651205e6

This note classifies external repositories supplied during the Testament project run. External code, prose, or corpora do not gain evidentiary authority merely because they are useful.

## 1. KKKKhazix/khazix-skills

Observed head:
- main: 4f2db09802736ac8130ddf8dd6121435b5a41b55
- license: MIT

Role:
- METHOD / AGENT-WORKFLOW INSPIRATION
- NOT HISTORICAL OR THEOLOGICAL EVIDENCE

Useful patterns:
- `leader`: explicit goal, completion state, evidence, anti-cheating constraints, bounded scope, stop conditions, and progress recovery.
- `neat-freak`: reconcile code/runtime/docs/rules/memory/workspace rather than treating a green test or clean Git state as total closure.
- `hv-analysis`: longitudinal + horizontal comparison is potentially useful as a research-organization pattern, but ON_THEO evidence contracts must override its opinionated writing/forecasting style.

Admission decision:
- ADMIT selected methods conceptually.
- DO NOT install or copy skills wholesale into Testament.
- Any historical/comparative use belongs upstream in ON_THEO and must preserve evidence classes and provenance.

## 2. yhatt/marp

Observed head:
- master: 5ce01a2343a28d25f25085d1d37cd92ea180184b
- repository state: archived
- license: MIT

The repository itself states that the classic Marp application is discontinued and warns of a serious security issue in the old app.

Maintained successor inspected:
- repository: marp-team/marp-cli
- main: ffc4128626cbc64965fe1cc805717c6d4438c384
- role: Markdown -> HTML/PDF/PPTX/images converter
- license: MIT

Role for Testament:
- OPTIONAL PRESENTATION / BRIEFING OUTPUT TOOL
- NOT MANUSCRIPT AUTHORING AUTHORITY
- NOT EVIDENCE

Admission decision:
- REJECT classic `yhatt/marp` for use.
- KEEP maintained Marp CLI as an optional future presentation adapter only.
- No current Testament dependency required.

## 3. cirosantilli/china-dictatorship

Observed head:
- master: dc9884711356ebfe3da729c516dd7e2e555b4419
- license: CC-BY-SA-4.0

The repository describes itself as an anti-Chinese-government propaganda/advocacy collection and contains a heterogeneous mixture of copied documents, commentary, political material, links, and site/mirroring infrastructure.

Role:
- DISCOVERY INDEX ONLY, if a future task specifically needs a document found there
- NO SOURCE AUTHORITY
- PUBLISHING / CORPUS-RESILIENCE METHOD INSPIRATION ONLY

Potentially reusable architectural patterns observed at the pinned head:
- one source corpus rendered into multiple HTML forms, including multipage output;
- media separated from the text repository;
- explicit mirror/push tooling for redundant publication;
- use of archived snapshots when live links may disappear;
- the same corpus exposed through more than one software packaging surface.

These are engineering/publishing patterns, not evidence and not endorsements of the repository's political framing or content.

Evidence rule:
- A document discovered there must be traced to its original or an independently reliable source before any factual claim is admitted.
- Repository aggregation, labels, commentary, or framing are not evidence for the underlying political or historical claims.

Admission decision:
- CONTENT remains NOT_ADMITTED to the active Testament evidence graph.
- ADMIT only the generic publication-resilience concepts for possible future Testament tooling.
- Do not copy its political corpus, source labels, or advocacy framing into Testament.
- No dependency on this repository is justified at present.

## 4. hughhowey/neo

Observed head:
- main: a2846ff28f8bfec257565c6ca0ecce4c16242e61
- version observed: 0.7.5
- license: MIT

NEO is a local Electron writing application. Its documented storage model is intentionally simple:
- one book folder;
- `book.json` metadata;
- `chapters/*.html`;
- JSON sidecars for darlings/stickies;
- no database or proprietary project format.

It also exposes author-oriented features relevant to Testament:
- distraction-free chapter editing;
- outline support;
- recoverable "Darlings";
- placeholders;
- local plain-file storage;
- EPUB/DOCX/PDF/HTML/Markdown/text export;
- autosave/backups.

Role:
- HIGH-VALUE OPTIONAL MANUSCRIPT FRONTEND / READER-EDITION EXPORT SURFACE
- NOT CANONICAL STATE
- NOT EVIDENCE

Proposed integration boundary:
`Testament GitHub Markdown -> deterministic adapter -> NEO library`

Initial integration should be one-way only.

Why:
- Testament must keep GitHub Markdown + apparatus/provenance as canonical state.
- NEO chapter HTML does not natively carry Testament evidence classes, source maps, review state, or exact upstream provenance.
- Bidirectional editing would create a second source of truth unless a deterministic round-trip and conflict protocol is built and tested.

Adapter requirements before use:
1. map Draft/reader-edition chapter Markdown into NEO chapter HTML;
2. preserve stable chapter IDs and order;
3. keep apparatus/source-control files outside the NEO reader surface unless explicitly rendered;
4. never infer that a NEO-edited sentence has passed source review;
5. if reverse sync is ever added, require explicit reconciliation and exact diff review before GitHub writeback.

Admission decision:
- ADMIT as a future presentation/editing adapter candidate.
- Strongest immediate candidate among the four repositories.
- Do not move canonical manuscript state into NEO.
- Concrete adapter contract: `docs/NEO_ADAPTER_SPEC_V1.md`.

## Portfolio result

- Khazix Skills: methodology inspiration, bounded.
- Classic Marp: reject; maintained Marp CLI may serve future slides.
- China Dictatorship repo: content not admitted; only generic corpus-publication resilience patterns retained as method inspiration.
- NEO: admitted as an optional manuscript frontend/export candidate with a strict one-way initial boundary; a prototype exporter and bounded test suite now exist on this draft branch.

No external repository is promoted into ON_THEO evidence by this evaluation.
No merge, installation, dependency addition, publication, or deployment is authorized or performed by this note.
