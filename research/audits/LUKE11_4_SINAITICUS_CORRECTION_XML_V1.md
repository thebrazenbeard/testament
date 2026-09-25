# Luke 11:4 — Codex Sinaiticus Correction-Layer XML Audit V1

Status: **DIRECT OFFICIAL LOCUS XML APPARATUS READBACK / CORRECTION CONFLICT RESOLVED AT PROJECT-ENCODING LEVEL / NOT MANUSCRIPT-IMAGE AUTOPSY**

## Scope

This audit resolves the prior Luke 11:4 Sinaiticus correction-state conflict by reading the official Codex Sinaiticus XML apparatus at the exact locus.

It does not claim fresh visual inspection of the manuscript pixels.

## Physical / XML locus

- witness: `WIT-01-CODEX-SINAITICUS`
- passage: Luke 11:4
- British Library folio: `236b`
- project page id: `78-5v`
- column: `4`
- verse id, v1.04: `V-B35K11V4-35-LUKE`
- verse id, v1.95: `V-B35K11V4-35-LUKE`
- relevant lines: 30–37

## Official source cuts

### Codex Sinaiticus Project v1.04 archive

- archive record: `https://epapers.bham.ac.uk/id/eprint/1886/`
- archive file: `FINAL_TRANSCRIPTION_version104.xml.zip`
- extracted XML bytes: `30238789`
- extracted XML SHA-256: `5f67c70c4c21ba905824fd2ff5ec3c21bf5358d36bb421ad9fda75e23ea9f0d4`
- exact Luke 11:4 `<ab>` chunk bytes: `1748`
- exact Luke 11:4 chunk SHA-256: `179c3574043c4d78755e89d73dbbc19e7912ab0f2e00d39e2d1677b9241e068d`

### ITSEE/Birmingham current public transcription repository

- repository: `itsee-birmingham/codex-sinaiticus`
- checked commit: `af1633b5102cbe6200e79053cc618ac447e1bb16`
- file: `sinaiticus_full_v195.xml`
- Git blob: `29cc37dcaa2216d16a5a6945c05e5813e147fb96`
- local fetched XML bytes: `51914270`
- local fetched XML SHA-256: `b676767c4511ff71393ade69cc6049e2731c235c1a08e7e106f45f00a6dd7233`
- exact Luke 11:4 `<ab>` chunk bytes: `2948`
- exact Luke 11:4 chunk SHA-256: `987c493a5179ff94e053a1102a5b663397c1c906e15425407ed26af58c51fa8f`

The v1.95 file enriches the markup but preserves the same correction-state content at the target locus.

## XML correction semantics

The Codex Sinaiticus Project XML specification states:
- the original reading is represented as the main/original reading;
- correction readings carry the corrector identity;
- a blank original/main reading means omission;
- a blank correction reading means deletion;
- multiple readings may occur in a single apparatus element.

In v1.95 the schema has been modernized to explicit `type="orig" hand="firsthand"` and `type="corr" hand="ca"`, which removes the earlier need to infer first-hand identity from display order at this locus.

## Direct Luke 11:4 apparatus readback

Immediately after the testing petition (`... εις πειρασμον`), v1.95 encodes:

1. first hand / original:
   - `<rdg type="orig" hand="firsthand"><w n="21"/></rdg>`
   - state: **blank / omitted**

2. `ca` correction reading:
   - `αλλα ρυσ(αι) ημας απο τ`
   - normalized only to the extent directly supported:
     - `ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τ…`
   - state: **partial deliverance-petition addition**

3. second encoded `ca` correction reading:
   - `<rdg type="corr" hand="ca"><w n="21"/></rdg>`
   - state under the project XML specification: **deletion**

v1.04 carries the same three-state content using `main-corr` plus two `corr n="ca"` readings.

## Critical boundary: the addition is partial

The official transcription does **not** encode a complete `ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ` at this locus.

It encodes only:

`αλλα ρυσ(αι) ημας απο τ`

ending at tau.

Therefore Testament must not silently expand the correction into the complete Matthean phrase.

Published apparatus summaries may describe the correction as a deliverance-petition reading, but the direct project XML is the controlling evidence for exactly what this audit claims.

## Hand / chronology ceiling

Directly established from project encoding:
- first hand omits the addition;
- a correction state assigned to `ca` contains the partial deliverance wording;
- another correction state assigned to `ca` is blank, which the project specification defines as deletion.

Not independently established:
- that the two `ca` readings represent two palaeographically distinguishable correctors rather than two encoded states assigned to the same correction class;
- a finer chronological sequence inside `ca` beyond the order represented in the apparatus;
- equivalence between the project's `ca` label and simplified external labels such as `corrector 1` / `corrector 2`;
- the complete text of a Matthean deliverance clause in the correction.

Therefore the safe project description is:

**FIRST HAND OMITS / `ca` CORRECTION LAYER CONTAINS A PARTIAL DELIVERANCE ADDITION / `ca` DELETION STATE ALSO ENCODED.**

## Relationship to the old conflict

Before this audit Testament had:
- the default official transcription showing the shorter ending;
- NET assigning longer/shorter states to simplified corrector labels;
- older secondary summaries giving a conflicting sequence.

The direct locus XML now outranks those secondary summaries for the Codex Sinaiticus Project's own correction encoding.

The older normalized hand-sequence claim remains withdrawn.

## Debt consequence

The evidence requirement behind:

`LUKE11_4_SINAITICUS_CORRECTION_POPUP_IMAGE_READBACK`

is technically satisfied by the explicitly allowed alternative:

`DIRECT LOCUS-SPECIFIC XML APPARATUS READBACK`.

Closure is subject to exact-head hostile review.

Separate image/autoptic work remains separate and must not be implied closed by this XML audit.

## Sources

- Codex Sinaiticus Project XML download / transcription archive.
- Codex Sinaiticus Project XML specification.
- Codex Sinaiticus Project transcription methodology.
- `itsee-birmingham/codex-sinaiticus` current public XML repository.

## Claim ceiling

Established:
- exact official XML locus;
- first-hand omission;
- partial `ca` deliverance addition through `... απο τ`;
- blank `ca` deletion state;
- v1.04 and v1.95 semantic agreement at the locus.

Not established:
- manuscript-pixel autopsy;
- full corrected Matthean deliverance wording;
- finer palaeographic chronology within `ca`;
- a forced reconciliation of external simplified corrector numbering with the Codex Sinaiticus Project hand labels.