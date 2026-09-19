# Luke 11:2 Spirit Petition — 162 / 700 Image Route V1

Status: ROUTE_BOUND / 162_EXACT_SIDE_RESOLVED / 700_FACSIMILE_INDEPENDENTLY_CROSS_BOUND / DIRECT_PIXEL_COLLATION_PENDING

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

### Hoskier 1890 scan-topology narrowing

The Internet Archive IIIF Presentation 3 manifest and OCR annotation service now narrow the two Hoskier facsimile leaves without guessing their identity.

Exact scan structure:
- canvas `28` contains Hoskier's printed NOTE identifying the two reproductions as:
  - folio 180r, Luke 9:48-54;
  - folio 184v, Luke 11:2-8;
- canvas `30` is the printed start of the Introduction;
- canvas `27` has only sparse/gibberish OCR consistent with a photographic manuscript plate;
- canvas `29` has an empty OCR annotation page;
- because Hoskier states that the two reproductions precede the Introduction, canvases 27 and 29 are the two isolated facsimile candidates surrounding the note and immediately preceding canvas 30.

Exact Internet Archive image services:
- candidate canvas 27 -> JP2 leaf `fullaccountcolla00hoskrich_0028.jp2`;
- printed note canvas 28 -> JP2 leaf `fullaccountcolla00hoskrich_0029.jp2`;
- candidate canvas 29 -> JP2 leaf `fullaccountcolla00hoskrich_0030.jp2`;
- Introduction canvas 30 -> JP2 leaf `fullaccountcolla00hoskrich_0031.jp2`.

Control:
- current evidence does **not** distinguish which of candidate canvases 27 and 29 is folio 180r versus folio 184v;
- plate order is therefore not inferred from Hoskier's prose order;
- neither candidate is promoted to the Luke 11:2 plate until visual or independent page-specific evidence identifies it.

This turns the Hoskier route from a 300-page volume into a two-image candidate set while preserving the remaining identity uncertainty.

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

Runtime boundary:
- the PDF text/extraction layer exposes the Plate X caption and its manuscript-page identification;
- the PDF screenshot endpoint repeatedly failed with a cache-miss error in the current runtime;
- therefore Testament does **not** claim fresh pixel/glyph inspection from Kenyon's plate in this pass.

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
- direct pixel readback of either witness at Luke 11:2;
- a fresh diplomatic transcription from either manuscript image;
- originality of the Spirit petition;
- identity of this family with Marcion's indirectly attested Spirit request.

## Debt result

`LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION` remains OPEN.

The debt is narrower:
- 162 exact side is resolved to 151v / p0314;
- 700 exact folio/side is resolved;
- 700 facsimile identity is independently cross-bound through Hoskier 1890 and Kenyon 1912;
- Hoskier's 300-page scan is narrowed to candidate facsimile canvases 27 and 29, with the Luke-11 plate assignment still unresolved;
- actual manuscript-pixel collation remains pending.

No facsimile caption, OCR layer, or published transcription is promoted into direct visual manuscript readback.
