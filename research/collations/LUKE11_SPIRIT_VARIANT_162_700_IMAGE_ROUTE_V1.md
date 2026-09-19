# Luke 11:2 Spirit Petition — 162 / 700 Image Route V1

Status: ROUTE_BOUND / DIRECT_PIXEL_COLLATION_PENDING

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
- eleventh century;
- Luke occupies ff. 145r-229v.

Exact historical facsimile target:
- H. C. Hoskier's 1890 full collation explicitly states that one of its two manuscript reproductions is **folio 184 verso, containing Luke 11:2-8**;
- this directly fixes the side that the prior Testament node left unspecified;
- the public-domain Hoskier volume is digitized on Wikimedia Commons / Internet Archive (`fullaccountcolla00hoskrich`).

Digitized-route control:
- Internet Archive IIIF manifest: `https://iiif.archive.org/iiif/fullaccountcolla00hoskrich/manifest.json`;
- Wikimedia Commons hosts the 300-page public-domain PDF and per-page rendered previews;
- front-matter scan analysis isolates the photographic facsimile leaves before the Introduction, but Testament does not promote a derivative scan-page guess into a direct manuscript reading.

Published wording control:
- Metzger reports 700: `ἐλθέτω τὸ πνεῦμά σου τὸ ἅγιον ἐφ’ ἡμᾶς καὶ καθαρισάτω ἡμᾶς`;
- the `ἐφ’ ἡμᾶς` phrase distinguishes 700 from 162 in this pair.

## Evidence ceiling

Established:
- both physical Greek witnesses are identified;
- their published forms are non-identical;
- 162 now has exact Vatican 151r/151v institutional image targets;
- 700's target is now exactly folio 184v, Luke 11:2-8, from Hoskier's facsimile description;
- public image/facsimile routes exist for both witnesses.

Not established in this runtime:
- direct pixel readback of either witness at Luke 11:2;
- whether 162's passage is on 151r or 151v;
- a fresh diplomatic transcription from either image;
- originality of the Spirit petition;
- identity of this family with Marcion's indirectly attested Spirit request.

## Debt result

`LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION` remains OPEN.

The debt is now narrower: image targets and 700's exact side are resolved; actual pixel collation remains pending.
