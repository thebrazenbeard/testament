# Hostile Review — Book III Hoskier / Kenyon Codex 700 Plate Identity — Tranche 55

Status: **PASS_FOR_TRANCHE_AFTER_TOPOLOGY_REPAIR / CODEX700_LUKE11_PLATE_IDENTITY_RESOLVED / DIRECT_GLYPH_COLLATION_OPEN**

Final review target:
- `25a4176f72756f1ac550caf4d3513574fa34a4d5`

Pre-repair target:
- `58a93edb83f4096aed88a994ffca6651dbe4febf`

Intermediate repair:
- `d4c41639a9dd9ddbd0cbb4da8da15575a3dc6f56`

Scope:
- `research/collations/CODEX700_HOSKIER_KENYON_PIXEL_CROSSBIND_V1.md`
- `research/collations/LUKE11_SPIRIT_VARIANT_162_700_IMAGE_ROUTE_V1.md`
- Hoskier 1890 public-domain scan
- Kenyon 1912 Plate X
- Codex 700 / Egerton MS 2610 / Luke 11:2-8
- `LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION`

## Finding

`HR-BIII-016_HOSKIER_FACSIMILE_CANDIDATE_TOPOLOGY`

Tranche 54 treated Hoskier scan pages/canvases 27 and 29 as the two facsimile candidates surrounding the printed note.

Fresh direct scan-page readback falsified that topology:
- page 25 is a manuscript-like plate;
- page 26 is effectively blank;
- page 27 is a high-contrast manuscript plate;
- page 28 is Hoskier's printed NOTE naming the two reproduced folios;
- page 29 is effectively blank / verso-like;
- page 30 begins the printed Introduction.

The two active reproduction candidates are therefore pages 25 and 27, not 27 and 29.

## Repair verification

PASS.

The repaired evidence subject:
- explicitly supersedes the 27/29 candidate-pair statement;
- records exact JPEG SHA-256 identities for pages 25-29;
- keeps Hoskier's own two-folio note distinct from scan-order inference;
- uses independently identified Kenyon Plate X as an image-identity anchor;
- does not promote OCR, captions, or image registration into a diplomatic Greek transcription.

Kenyon scan page 175 directly binds Plate X to:
- Codex 700 / British Museum Egerton MS 2610;
- Luke xi. 2-8;
- the remarkable second-petition Spirit reading.

## Pixel-registration falsification

Initial normalized registration against Kenyon Plate X:
- Hoskier page 27: **0.3124** under 180-degree rotation;
- Hoskier page 25: **0.0889**;
- Hoskier page 29: **0.0430**.

A broader hostile control then compared Kenyon Plate X against every surrounding Hoskier scan page 22-35:
- page 27: **0.2978**;
- next-highest page 30: **0.1486**;
- page 28: **0.1486**;
- page 24: **0.1469**;
- page 25: **0.1033**;
- page 29: **0.0423**.

Page 27 remains the clear neighborhood outlier. The result is not dependent on comparing only the preferred candidates.

## Identity result

PASS for image identity:
- **Hoskier page/canvas 27 = folio 184v = Luke 11:2-8**;
- **Hoskier page/canvas 25 = folio 180r = Luke 9:48-54**.

This resolves the Codex 700 Hoskier plate-identity subfrontier.

## Direct-image boundary

Still OPEN:
- fresh diplomatic Greek transcription of the Spirit petition on Hoskier page 27;
- direct manuscript-image collation of GA 162 at Luke 11:2;
- full `LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION`.

The repaired files explicitly preserve `DIRECT_GLYPH_COLLATION_PENDING` and the full debt remains OPEN.

## Provenance consistency

PASS after intermediate repair.

The first repair commit still contained a stale statement saying Kenyon pixels were unavailable. Exact head `25a4176f72756f1ac550caf4d3513574fa34a4d5` corrects that:
- direct Internet Archive JPEG pixels for Kenyon scan page 175 were retrieved;
- those pixels were used for image-identity registration;
- they were not used to claim a fresh diplomatic Greek transcription.

## Repository checks

- PR #1 remains OPEN / DRAFT / UNMERGED.
- Exact reviewed head: `25a4176f72756f1ac550caf4d3513574fa34a4d5`.
- GitHub reports mergeable=true at review readback.
- No commit statuses reported.
- No pull-request-triggered workflow runs reported.
- The reviewed delta from `58a93edb...` changes only the Codex 700 cross-bind artifact and the 162/700 route collation.

## Debt disposition

Repaired finding:
- `HR-BIII-016_HOSKIER_FACSIMILE_CANDIDATE_TOPOLOGY`

Closed subfrontier:
- `CODEX700_HOSKIER_LUKE11_PLATE_IDENTITY`

Residual debt:
- `LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION`
- `IMAGE_AUTOPTIC_LEVEL_VERIFICATION`
- `P46_1COR7_10_11_VISUAL_PIXEL_COLLATION`

## Verdict

`PASS_FOR_TRANCHE_AFTER_TOPOLOGY_REPAIR / CODEX700_LUKE11_PLATE_IDENTITY_RESOLVED / DIRECT_GLYPH_COLLATION_OPEN`

No merge, manuscript promotion, publication, deployment, spend, provider mutation, or other protected effect is authorized or claimed.
