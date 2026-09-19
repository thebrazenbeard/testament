# Luke 17:21 Versional Text Collation V1

Status: DIRECT_VERSIONAL_TEXT_COLLATION_BOUND / OLD_SYRIAC_CAL_DIRECT_BOUND / HARKLEAN_PUBLISHED_PAGE_VISUAL_READBACK_BOUND

Purpose:
- distinguish versional strings directly readable in current accessible editions from forms known only through published comparative-edition reporting;
- prevent "Syriac reception" from being treated as one flat witness;
- narrow the remaining Luke 17:21 versional debt to the exact streams still lacking stable direct text encoding.

Greek target:
- `entos hymon` in Luke 17:21.

## Latin — Vulgate

Direct accessible text:
- `neque dicent: Ecce hic, aut ecce illic. Ecce enim regnum Dei intra vos est.`

Target rendering:
- `intra vos`

State:
- DIRECT_TEXT_COLLATION_BOUND

Semantic observation:
- `intra` is an interior/bounded Latin preposition.

Guard:
- a Latin translator's choice is evidence for reception/translation history, not proof of Luke's Greek intent.

Direct source:
- public Vulgate text at Luke 17:21.

## Latin — Vetus Latina / Bezae Latin column

Published report:
- Ramelli reports `intra vos` across the Old Latin witnesses discussed, including the Bezae Latin column.

State:
- EDITION_REPORTED_NOT_DIRECTLY_COLLATION_BOUND

Guard:
- do not upgrade the Old Latin collective to direct Testament collation from a Vulgate readback.

## Syriac — Peshitta

Direct accessible text:
- `ܘܠܐ ܐܡܪܝܢ ܗܐ ܗܪܟܐ ܗܝ ܘܗܐ ܗܪ ܬܡܢ ܗܝ ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܠܓܘ ܡܢܟܘܢ ܗܝ`

Target rendering:
- `ܠܓܘ ܡܢܟܘܢ`

State:
- DIRECT_TEXT_COLLATION_BOUND

Published semantic report:
- Ramelli analyzes the Peshitta expression as an explicit inside/interior rendering derived from the Syriac noun for the inside/inner parts.

Guard:
- direct text readback establishes the versional string;
- the semantic analysis remains a lexical/scholarly interpretation and does not settle Luke's Greek by itself.

Direct source:
- public Peshitta text at Luke 17:21.

## Syriac — Old Syriac Sinaitic + Curetonian

Edition anchor:
- George A. Kiraz, *Comparative Edition of the Syriac Gospels*, vol. 3, p. 352.

Direct computational text anchor:
- Comprehensive Aramaic Lexicon-derived Old Syriac corpus at `chenzhan4321/diatessaron-synopsis`, pinned to commit `6b165111c292aaa128272ff0d2daeb866986c0d7`;
- Curetonian file `data/cal_old_syriac/LkCur.tsv`, blob `768adf5651583b842cf4192367527a77687be696`;
- Sinaiticus file `data/cal_old_syriac/LkSin.tsv`, blob `7facf587c87237320defef3980872bc3b2749a32`;
- CAL→Syriac converter `scripts/cal_to_syriac.py`, blob `49099dc8dae6ba6c7bf2d965fb3d0dfbb69edf39`.

Direct CAL rows:
- Curetonian Luke 17:21:
  `wl) n)mrwn h) hrk) hy )w h) hrtmn hy, h) gyr mlkwth d)lh) byntkwn%`
- Sinaiticus Luke 17:21:
  `wl) )mryn hrk) hy )w hrtmn hy h) gyr mlkwth d)lh) byntkwn,`

Shared target expression:
- direct CAL: `byntkwn`;
- mechanically derived Unicode through the pinned one-to-one converter: `ܒܝܢܬܟܘܢ`.

Critical source-quality finding:
- the public corpus's stored Syriac-script field is **not usable at this locus**;
- both Luke 17:21 rows carry an unrelated Syriac string in that field;
- the converter's own documentation explains that scraped Syriac-script fields suffered verse-number misalignment and explicitly treats CAL romanization as the reliable ground truth;
- Testament therefore rejects the source Unicode field and never cites it as Luke 17:21 text.

Published semantic report:
- Ramelli reports that Sinaiticus and Curetonianus have the same Luke 17:21b wording;
- the relevant Old Syriac expression can carry within/inside or between/among senses.

State:
- DIRECT_CAL_ROMANIZATION_BOUND / TARGET_EXPRESSION_UNICODE_REPRODUCIBLY_DERIVED / SOURCE_UNICODE_COLUMN_REJECTED_AS_MISALIGNED

Guard:
- `ܒܝܢܬܟܘܢ` is a deterministic script conversion of the directly bound CAL token `byntkwn`, not a direct Unicode readback from the manuscript or from the broken source Unicode column;
- Curetonian's trailing `%` marker is preserved as unresolved source encoding rather than silently normalized;
- Old Syriac remains semantically ambiguous in the project;
- script conversion does not decide whether the expression should be translated "within" or "among."

## Syriac — Harklean

Edition anchor:
- George A. Kiraz, *Comparative Edition of the Syriac Gospels*, vol. 3, p. 352.
- Ramelli explicitly cites this locus for Luke 17:21b and notes that Kiraz's Harklean text is based primarily on Vat. Syr. 268.

Published-page direct visual readback:
- Ramelli, *Hugoye* 12.2 (2009), p. 264, directly prints the Harklean Luke 17:21b line.
- the PDF text extractor corrupts the Syriac font, so Testament did not use extracted mojibake as the reading;
- the rendered PDF page was inspected visually;
- the adjacent Peshitta line on the same page was used as a calibration control because its Unicode wording is independently bound elsewhere in this project;
- the old-font glyph stream decodes consistently against that Peshitta control and then resolves the Harklean line without ad hoc substitutions.

Direct stable Unicode encoding:
- `ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܒܓܘܟܘܢ ܐܝܬܝܗ`

Decode audit:
- `research/audits/LUKE17_21_HARKLEAN_FONT_DECODE_V1.md`
- same-page Peshitta calibration fixes the legacy font mapping;
- a terminal ASCII `J` in the extracted legacy-font stream is classified as a nonlexical extraction artifact because it recurs at another Syriac quotation boundary and is not required by the rendered line.

Target expression:
- `ܒܓܘܟܘܢ`

Independent target control:
- the Syriac Orthodox Patriarchate's digital Bar Hebraeus Luke commentary prints the base Luke 17:21 wording with `ܡܠܟܘܬܗ ܕܐܠܗܐ` and then marks `ܒܓܘܟܘܢ ܐܝܬܝܗ` as the Greek-aligned form;
- this corroborates the target sequence and kingdom-word spelling without being promoted to an independent Harklean manuscript witness.

Font-decoding control:
- Peshitta printed `ܠܓܘ ܡܢܟܘܢ` on the same page yields the expected reverse-glyph sequence under the custom Syriac font;
- the Harklean custom-font sequence correspondingly resolves to `ܒܓܘܟܘܢ`;
- the final Harklean copula resolves to `ܐܝܬܝܗ`.

State:
- DIRECT_PUBLISHED_PAGE_VISUAL_READBACK / STABLE_UNICODE_ENCODING_BOUND / NOT_MANUSCRIPT_AUTOPSY

Semantic report:
- Ramelli argues that Harklean `ܒܓܘܟܘܢ` is an explicit inside/interior rendering and contrasts the version's wording with Syriac renderings of Greek `en mesō + genitive`.

Guard:
- this is direct readback of a published scholarly page reproducing the Harklean text, not direct image autopsy of Vat. Syr. 268;
- the stable Unicode encoding establishes the versional wording;
- Ramelli's lexical interpretation remains scholarly analysis and does not, by itself, settle the Greek `entos hymon` dispute.

## Cross-version result

Directly collated in current project:
- Vulgate: `intra vos`
- Peshitta: `ܠܓܘ ܡܢܟܘܢ`

Direct CAL text / reproducibly derived target script:
- Old Syriac Sinaiticus: `byntkwn` → `ܒܝܢܬܟܘܢ`
- Old Syriac Curetonian: `byntkwn` → `ܒܝܢܬܟܘܢ`

Direct published-page visual readback / stable Unicode:
- Harklean: `ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܒܓܘܟܘܢ ܐܝܬܝܗ`

Edition-reported but not yet directly machine-bound:
- Vetus Latina collective / Bezae Latin column

Debt disposition proposed by this unit:
- `LUKE17_21_OLD_SYRIAC_HARKLEAN_DIRECT_TEXT_ENCODING` can close after exact-head hostile review;
- Old Syriac is already directly bound at CAL-romanization level with deterministic script conversion;
- Harklean now has direct published-page visual readback and stable Unicode encoding.

The Old Latin collective remains a lower-level expansion item under broader versional/patristic debt rather than blocking this specific Syriac target.

## Evidence ceiling

Established:
- direct Vulgate string;
- direct Peshitta string;
- exact Kiraz edition locus used by Ramelli for the four Syriac versions;
- exact CAL-romanized Luke 17:21 rows for Old Syriac Curetonian and Sinaiticus from pinned public corpus blobs;
- shared Old Syriac target token `byntkwn`;
- reproducible CAL→Unicode target conversion `ܒܝܢܬܟܘܢ`;
- the public corpus's stored Syriac-script field is misaligned at this locus and must not be used;
- Old Syriac semantic ambiguity as reported;
- stable Harklean Unicode line from direct visual readback of Ramelli's published reproduction of Kiraz's text;
- Harklean target expression `ܒܓܘܟܘܢ`;
- Harklean/Peshitta interior-rendering argument as reported.

Not established:
- direct manuscript-image readback of Old Syriac Luke 17:21;
- direct source-native Unicode Old Syriac verse text at this locus;
- direct manuscript-image readback of the Harklean base manuscript;
- manuscript-image autopsy of Sinaiticus, Curetonianus, or Vat. Syr. 268;
- final translation of Greek `entos hymon`.

## Sources

- George A. Kiraz, ed., *Comparative Edition of the Syriac Gospels*, vol. 3: Luke (Brill, 1996), p. 352.
- Ilaria Ramelli, "Luke 17:21: The Kingdom of God is Inside You," *Hugoye* 12, 259–286, DOI 10.31826/hug-2011-120112.
- Direct published-page readback locus: Ramelli PDF p. 264 (journal pagination), Harklean quotation derived from Kiraz vol. 3 p. 352.
- Independent Syriac control: Syriac Orthodox Patriarchate digital Bar Hebraeus commentary on Luke 17:21.
- Syriaca.org bibliographic record for Kiraz, Luke, vol. 3.
- public Peshitta Luke 17:21 text.
- public Vulgate Luke 17:21 text.


## Old Syriac computational provenance — 2026-09-19

The CAL-derived public corpus is useful only after separating its reliable and defective layers.

Reliable:
- reference-aligned CAL romanization rows;
- pinned Git blobs;
- deterministic CAL letter mapping.

Rejected:
- stored Syriac Unicode verse field at Luke 17:21, because it contains text from a different verse.

The converter source itself documents the same defect class: right-to-left verse-number handling caused mismatched Syriac-script verse assignments, so CAL romanization is treated as ground truth.

This is exactly why Testament binds:
**direct CAL source text → deterministic target-script derivation → separate semantic interpretation**.

It does not label a generated Unicode rendering as manuscript autopsy or source-native Unicode.
