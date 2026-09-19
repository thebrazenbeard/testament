# Luke 11:2 Spirit Petition — 162 / 700 Image Route V1

Status: ROUTE_BOUND / 162_EXACT_SIDE_RESOLVED / 700_HOSKIER_PLATE_IDENTITY_RESOLVED / DIRECT_GLYPH_COLLATION_PENDING

Scope:
- WIT-162-BARB-GR-449
- WIT-700-EGERTON-2610
- Luke 11:2 kingdom-substitution / Holy-Spirit petition

## Witness 162 — Vatican Barb.gr.449

Source/witness identity:
- Gregory-Aland 162;
- Vatican Apostolic Library, Barb.gr.449;
- colophon dated 13 May 1153;
- Luke occupies ff. 119r-187v.

Exact institutional image target:
- Luke 11:2 is independently localized to **folio 151v**;
- DigiVatLib page: `https://digi.vatlib.it/view/MSS_Barb.gr.449/0314`;
- DigiVatLib canvas: `p0314`;
- folio 151v image service: `https://digi.vatlib.it/iiifimage/MSS_Barb.gr.449/Barb.gr.449_0314_fa_0151v.jp2`;
- manifest: `https://digi.vatlib.it/iiif/MSS_Barb.gr.449/manifest.json`.

Independent side cross-bind:
- James Snapp Jr., "Fifty Manuscripts at the Vatican Library" explicitly states: GA 162 / Barb.gr.449, Luke 11:2 is on **151v**;
- his 2021 selective page index links Luke 11:1 to DigiVatLib `/0313` and Luke 11:2 to DigiVatLib `/0314`;
- the same 2021 discussion identifies the Luke 11:2 Spirit-petition reading in GA 162 and notes support from GA 700.

Sources:
- `https://www.thetextofthegospels.com/2016/09/fifty-manuscripts-at-vatican-library.html`
- `https://www.thetextofthegospels.com/2021/01/hand-to-hand-combat-sinaiticus-vs-162.html`
- `https://digi.vatlib.it/view/MSS_Barb.gr.449/0314`

Pass result:
- the old 151r/151v ambiguity is closed;
- `p0314 / 151v` is the exact Luke 11:2 image target;
- the Vatican viewer and IIIF service resolve at route level;
- current non-metered extraction still does not deliver the manuscript pixels into the visual inspection surface;
- therefore exact side is resolved but direct image reading remains pending.

Published wording control:
- Metzger reports 162 as agreeing with the Spirit-petition family while differing from 700 in possessive order and omission of `ἐφ’ ἡμᾶς`.

## Witness 700 — British Library Egerton MS 2610

Source/witness identity:
- Gregory-Aland 700 / Scrivener 604;
- British Library, Egerton MS 2610;
- eleventh/twelfth-century minuscule witness;
- Luke occupies ff. 145r-229v.

### Hoskier 1890 facsimile target

H. C. Hoskier's 1890 full collation explicitly states that one of its two manuscript reproductions is **folio 184 verso, containing Luke 11:2-8**.

This:
- fixes the exact side that the prior Testament node left unspecified;
- binds the target to the public-domain Hoskier volume digitized on Wikimedia Commons / Internet Archive (`fullaccountcolla00hoskrich`).

Digitized-route control:
- Internet Archive IIIF manifest: `https://iiif.archive.org/iiif/fullaccountcolla00hoskrich/manifest.json`;
- Wikimedia Commons hosts the 300-page public-domain PDF and per-page rendered previews;
- front-matter scan analysis isolates the photographic facsimile leaves before the Introduction, but Testament does not promote a derivative scan-page guess into a direct manuscript reading.

### Hoskier 1890 scan-topology correction and Plate-X pixel cross-bind

Tranche 54 correctly narrowed the facsimile neighborhood but misidentified the second candidate leaf. Fresh direct scan-page inspection shows the active candidate pair is **canvas/page 25 and canvas/page 27**, not 27 and 29.

Fresh Internet Archive page evidence:
- page `25`: low-contrast manuscript-like plate; sparse OCR/noise; JPEG SHA-256 `2490021241b80ded626217926a0d65ba723b38464369346af5b770345931b4b9`;
- page `26`: effectively blank intervening leaf; JPEG SHA-256 `24b9b17ac765facc01228b1216d100832a989f1358179feb0517ef6680503874`;
- page `27`: high-contrast manuscript plate; JPEG SHA-256 `1a0778f919464c3f9d5cad3d300375589fdcaa81d251b9deed70583f93672ef6`;
- page `28`: Hoskier's printed NOTE naming the two reproductions as folio 180r / Luke 9:48-54 and folio 184v / Luke 11:2-8;
- page `29`: effectively blank/verso-like leaf with no OCR text; JPEG SHA-256 `5a32d445bc7f7724c4a9bec19ceed97509b7ad33062969a2f13a005d93f9be56`;
- page `30`: printed start of the Introduction.

This supersedes the tranche-54 topology statement that treated pages 27 and 29 as the two facsimile candidates.

Kenyon's independently identified Plate X was then used as an image-identity cross-bind:
- Internet Archive scan page `175` of Kenyon's *Handbook to the Textual Criticism of the New Testament* contains Plate X;
- its OCR caption explicitly identifies `CODEX 700 (Brit. Mus. Egerton MS. 2610)` and states that the shown page contains Luke xi. 2-8;
- Kenyon page-175 JPEG SHA-256: `6a72f3cc3071c64a8b5df31ddb27a809f74d84e6efb159b9846925107ca83707`.

A high-pass, contrast-normalized image registration was run against Hoskier pages 25, 27, and 29 after scan-margin normalization. Best normalized correlations to Kenyon Plate X were:
- Hoskier 27: **0.3124**, best under 180-degree rotation;
- Hoskier 25: **0.0889**;
- Hoskier 29: **0.0430**.

The >3.5x separation over the other actual manuscript candidate, together with Kenyon's independent Luke 11:2-8 caption and Hoskier's exact two-reproduction note, resolves the Hoskier assignment:
- **page/canvas 27 = folio 184v = Luke 11:2-8**;
- **page/canvas 25 = folio 180r = Luke 9:48-54**.

Evidence boundary:
- this is direct pixel-level image identity/registration evidence;
- it is **not** a fresh diplomatic reading of the Greek letters;
- no Spirit-petition glyph sequence is promoted from image registration alone;
- the remaining debt is direct line/glyph collation on the now-resolved folio-184v plate, plus the separate GA 162 image side.

Durable methodological detail is recorded in:
`research/collations/CODEX700_HOSKIER_KENYON_PIXEL_CROSSBIND_V1.md`.

### Kenyon 1912 independent facsimile cross-bind

Frederic G. Kenyon's 1912 second edition of *Handbook to the Textual Criticism of the New Testament* independently reproduces Codex 700 as **Plate X**.

Public-domain digitized source:
- `https://www.confessionalbibliology.com/wp-content/uploads/2016/04/Handbook_to_the_textual_criticism_of_the.pdf`

The digitized public-domain edition:
- identifies Plate X as `CODEX 700 (Brit. Mus. Egerton MS. 2610)`;
- states that the reproduced page contains **Luke xi. 2-8**;
- explicitly identifies the remarkable second-petition Spirit reading on that reproduced page;
- places the plate facing printed page 139;
- separately describes manuscript 700 and cites Hoskier's collation.

This is independent facsimile/publication cross-binding of:
`Codex 700 -> Egerton MS 2610 -> reproduced manuscript page -> Luke 11:2-8 -> Spirit-petition locus`.

It materially strengthens target identity and removes dependence on one facsimile-description chain.

Runtime update:
- the earlier PDF screenshot endpoint remained unreliable;
- a direct Internet Archive JPEG route for Kenyon scan page 175 was subsequently resolved and the Plate X pixels were retrieved;
- those pixels were used only for image-identity registration against Hoskier's scan, not for a fresh diplomatic Greek transcription;
- the exact Kenyon JPEG SHA-256 is `6a72f3cc3071c64a8b5df31ddb27a809f74d84e6efb159b9846925107ca83707`.

Published wording control:
- Metzger reports 700: `ἐλθέτω τὸ πνεῦμά σου τὸ ἅγιον ἐφ’ ἡμᾶς καὶ καθαρισάτω ἡμᾶς`;
- Kenyon's Plate X caption independently identifies the same Spirit-petition locus in the reproduced manuscript page;
- the `ἐφ’ ἡμᾶς` phrase distinguishes 700 from 162 in this pair.

## Evidence ceiling

Established:
- both physical Greek witnesses are identified;
- their published forms are non-identical;
- 162's Luke 11:2 target is exactly Vatican Barb.gr.449 folio 151v / DigiVatLib p0314;
- 700's target is exactly folio 184v, Luke 11:2-8, under the Hoskier facsimile description;
- Kenyon 1912 independently reproduces Codex 700 as Plate X and identifies the reproduced page as Luke 11:2-8 with the Spirit-petition variant;
- public image/facsimile routes exist for both witnesses.

Not established in this runtime:
- a fresh diplomatic Greek transcription from either manuscript image;
- direct line/glyph collation of the Spirit-petition wording on Hoskier page 27;
- direct manuscript-image collation of GA 162 at Luke 11:2;
- originality of the Spirit petition;
- identity of this family with Marcion's indirectly attested Spirit request.

## Debt result

`LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION` remains OPEN.

The debt is narrower:
- 162 exact side is resolved to 151v / p0314;
- 700 exact folio/side is resolved;
- 700 facsimile identity is independently cross-bound through Hoskier 1890 and Kenyon 1912;
- Hoskier's Luke 11:2-8 reproduction is resolved to page/canvas 27 by pixel registration against independently identified Kenyon Plate X;
- Hoskier page/canvas 25 is thereby assigned to folio 180r / Luke 9:48-54;
- direct Greek line/glyph collation remains pending.

No facsimile caption, OCR layer, or published transcription is promoted into direct visual manuscript readback.
