# Codex 700 — Hoskier / Kenyon Pixel Cross-Bind V1

Status: **PLATE_IDENTITY_RESOLVED / DIRECT_GLYPH_TRANSCRIPTION_PENDING**

Date: 2026-09-19
Project: Testament
Exact predecessor head: `58a93edb83f4096aed88a994ffca6651dbe4febf`

## Question

Hoskier (1890) states that two reproductions preceding the Introduction show:
- folio 180r / Luke 9:48-54;
- folio 184v / Luke 11:2-8.

Tranche 54 had narrowed the candidates to scan canvases 27 and 29, but had not identified which was Luke 11.

## Fresh scan topology

Direct Internet Archive JPEG readback of the surrounding leaves shows:

| scan page | bytes | dimensions | pixel character | SHA-256 |
|---|---:|---:|---|---|
| 25 | 681634 | 2626x4022 | low-contrast manuscript-like plate | `2490021241b80ded626217926a0d65ba723b38464369346af5b770345931b4b9` |
| 26 | 413279 | 2626x4022 | effectively blank | `24b9b17ac765facc01228b1216d100832a989f1358179feb0517ef6680503874` |
| 27 | 908613 | 2626x4022 | high-contrast manuscript plate | `1a0778f919464c3f9d5cad3d300375589fdcaa81d251b9deed70583f93672ef6` |
| 28 | 655687 | 2626x4022 | printed Hoskier NOTE | `fa8ddb12a1e3c58b38e084b79674c5dc767fabd92c712fb863c0c0e874e12c9d` |
| 29 | 648657 | 2626x4022 | effectively blank / verso-like | `5a32d445bc7f7724c4a9bec19ceed97509b7ad33062969a2f13a005d93f9be56` |
| 30 | — | — | printed Introduction begins | — |

The OCR layer independently supports this topology:
- 25: sparse plate-like OCR noise;
- 26: no OCR text;
- 27: sparse plate-like OCR noise;
- 28: Hoskier NOTE naming the two reproduced folios;
- 29: no OCR text;
- 30: Introduction prose.

Therefore pages 25 and 27, not 27 and 29, are the two reproduction candidates.

## Independent Kenyon identity anchor

Kenyon (1912), *Handbook to the Textual Criticism of the New Testament*, scan page 175:
- OCR heading: `PLATE X`;
- caption: `CODEX 700 (Brit. Mus. Egerton MS. 2610)`;
- caption states that the page shown contains Luke xi. 2-8 and identifies the remarkable second-petition Spirit reading;
- JPEG SHA-256: `6a72f3cc3071c64a8b5df31ddb27a809f74d84e6efb159b9846925107ca83707`.

This gives an independent image of the exact Hoskier target page identity.

## Pixel registration

Method:
1. grayscale source images;
2. percentile contrast normalization;
3. Gaussian high-pass extraction to suppress scan-background gradients;
4. scan-margin normalization;
5. common-size resampling;
6. normalized image correlation with small translation search and 0/180-degree orientation search.

Best normalized correlation against Kenyon Plate X:
- Hoskier page 27: **0.3124** under 180-degree rotation;
- Hoskier page 25: **0.0889**;
- Hoskier page 29: **0.0430**.

The page-27 match is more than 3.5 times the other actual manuscript candidate and more than 7 times the blank/verso-like page 29.

## Result

Resolved:
- `Hoskier page/canvas 27 = folio 184v = Luke 11:2-8`;
- `Hoskier page/canvas 25 = folio 180r = Luke 9:48-54`.

Superseded:
- tranche-54 statement that canvases 27 and 29 were the two facsimile candidates.

Still open:
- direct Greek line/glyph reading of the Spirit petition from Hoskier page 27;
- direct manuscript-image collation of GA 162 at Luke 11:2;
- full `LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION`.

## Claim ceiling

This is image-identity evidence. It does not:
- transcribe Greek glyphs;
- establish originality of the Spirit petition;
- identify the 162/700 family with Marcion;
- close the full direct-image collation debt.

Sources:
- Internet Archive Hoskier item `fullaccountcolla00hoskrich`;
- Internet Archive Kenyon item `handbooktotextua00kenyrich`;
- Hoskier printed NOTE at scan page 28;
- Kenyon Plate X at scan page 175.
