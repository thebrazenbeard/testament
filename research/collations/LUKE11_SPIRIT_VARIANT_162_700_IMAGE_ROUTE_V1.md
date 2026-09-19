# Luke 11:2 Spirit Petition — 162 / 700 Image Route V1

Status: ROUTE_BOUND / 700_FACSIMILE_INDEPENDENTLY_CROSS_BOUND / DIRECT_PIXEL_COLLATION_PENDING

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

Exact institutional image targets:
- folio 151r: DigiVatLib canvas `p0313`;
- folio 151r image service: `https://digi.vatlib.it/iiifimage/MSS_Barb.gr.449/Barb.gr.449_0313_fa_0151r.jp2`;
- folio 151v: DigiVatLib canvas `p0314`;
- folio 151v image service: `https://digi.vatlib.it/iiifimage/MSS_Barb.gr.449/Barb.gr.449_0314_fa_0151v.jp2`;
- manifest: `https://digi.vatlib.it/iiif/MSS_Barb.gr.449/manifest.json`.

Pass result:
- the old folio-only locator is now reduced to an exact two-canvas target;
- the current scholarly passage locator does not itself specify recto versus verso;
- current runtime extraction resolves the institutional pages/services but does not deliver manuscript pixels for reliable visual collation;
- therefore the passage side and image reading remain pending rather than inferred.

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

### Kenyon 1912 independent facsimile cross-bind

Frederic G. Kenyon's 1912 second edition of *Handbook to the Textual Criticism of the New Testament* independently reproduces Codex 700 as **Plate X**.\n\nPublic-domain digitized source:\n- `https://www.confessionalbibliology.com/wp-content/uploads/2016/04/Handbook_to_the_textual_criticism_of_the.pdf`

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
- 162 has exact Vatican 151r/151v institutional image targets;
- 700's target is exactly folio 184v, Luke 11:2-8, under the Hoskier facsimile description;
- Kenyon 1912 independently reproduces Codex 700 as Plate X and identifies the reproduced page as Luke 11:2-8 with the Spirit-petition variant;
- public image/facsimile routes exist for both witnesses.

Not established in this runtime:
- direct pixel readback of either witness at Luke 11:2;
- whether 162's passage is on 151r or 151v;
- a fresh diplomatic transcription from either manuscript image;
- originality of the Spirit petition;
- identity of this family with Marcion's indirectly attested Spirit request.

## Debt result

`LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION` remains OPEN.

The debt is narrower:
- 162 image target pair is exact;
- 700 exact folio/side is resolved;
- 700 facsimile identity is independently cross-bound through Hoskier 1890 and Kenyon 1912;
- actual manuscript-pixel collation remains pending.

No facsimile caption, OCR layer, or published transcription is promoted into direct visual manuscript readback.
