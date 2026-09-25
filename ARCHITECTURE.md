# Repository Architecture

## Three-layer model

### 1. Evidence layer

Located primarily upstream in On-Theo and mirrored here only through dependency records and passage-level citations.

Contains:
- source identity;
- witness identity;
- dating;
- material evidence;
- transmission relations;
- scholarly disagreement;
- claim status.

### 2. Reconstruction layer

Located under research/ and apparatus/.

Contains:
- historical baselines;
- chronology;
- source matrices;
- competing reconstructions;
- convergence and divergence analysis;
- scene evidence packets;
- open questions.

### 3. Authored layer

Located under manuscript/.

Contains:
- narrative;
- reconstructed speeches;
- authorial interpretation;
- literary compression;
- speculative theology where clearly signaled.

## Directory map

- docs/ — project theory, epistemic rules, style, narrative design
- research/ — research plans, source universe, chronology, historical matrices
- apparatus/ — passage-level provenance and authorial-construction records
- schema/ — machine-readable record contracts
- manuscript/ — book outlines and eventual prose
- convergence/ — cross-tradition convergence/divergence analyses
- sources/ — local source metadata and dependency snapshots, not copied copyrighted corpora

## Promotion model

Foundation material develops through reviewed branches. No draft status implies historical acceptance.

Every manuscript passage should eventually be able to answer:
- What source(s) are behind this?
- How early are they?
- Are they independent?
- What conflicts with them?
- What did the author invent?
- Is a systems/simulation interpretation being applied?
