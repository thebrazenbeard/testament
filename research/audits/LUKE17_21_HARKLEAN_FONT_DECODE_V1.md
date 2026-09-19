# Luke 17:21 Harklean Published-Page Decode Audit V1

Status: **REPRODUCIBLE PUBLISHED-PAGE TEXT BINDING / NOT MANUSCRIPT AUTOPSY**

## Scope

This audit records how Testament recovered a stable Unicode encoding of the Harklean Luke 17:21b quotation printed by Ilaria Ramelli from George A. Kiraz's comparative edition.

It does not claim direct inspection of Vat. Syr. 268.

## Primary published locus

- Ilaria Ramelli, “Luke 17:21: ‘The Kingdom of God is Inside You’: The Ancient Syriac Versions in Support of the Correct Translation,” *Hugoye* 12.2 (2009), journal p. 264.
- Ramelli explicitly cites George A. Kiraz, *Comparative Edition of the Syriac Gospels*, vol. 3, p. 352 for Luke 17:21b.
- Ramelli states that Kiraz's Harklean text is based primarily on Vat. Syr. 268.
- public PDF: `https://hugoye.bethmardutho.org/pdf/vol12/HV12N2Ramelli.pdf`

## Access defect

The PDF's embedded legacy Syriac font does not extract as Unicode Syriac. Text extraction produces mojibake byte/glyph sequences.

Testament therefore does not treat the extracted mojibake as text.

## Calibration control

Ramelli prints the Peshitta immediately before the Harklean quotation on the same rendered page.

The Peshitta Luke 17:21 wording is independently Unicode-bound in Testament:

`ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܠܓܘ ܡܢܟܘܢ ܗܝ`

That independently known line provides a same-font calibration key for the legacy glyph stream.

Mapped lexical units include:
- legacy `ûÙÄ` -> `ܓܝܪ`;
- legacy `ÍÝàâ` -> `ܡܠܟܘܬܗ`;
- legacy `¿Ìß~` -> `ܕܐܠܗܐ`;
- legacy `ÍÅß` -> `ܠܓܘ`;
- legacy `ÍÝæâ` -> `ܡܢܟܘܢ`.

The calibration is not inferred from the Harklean semantics. It is fixed by a separate text whose Unicode form is independently available.

## Harklean decode

Applying the same glyph mapping to Ramelli's immediately adjacent Harklean quotation yields:

`ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܒܓܘܟܘܢ ܐܝܬܝܗ`

Target phrase:

`ܒܓܘܟܘܢ ܐܝܬܝܗ`

The key Harklean preposition is therefore `ܒܓܘ`, not Peshitta `ܠܓܘ ܡܢ` and not Old Syriac `ܒܝܢ`.

## Stray `J` extraction artifact

The Harklean extracted glyph stream contains a terminal ASCII `J` after the kingdom word sequence in the PDF text layer.

Testament does **not** decode that `J` as an additional Syriac letter because:
1. the rendered Syriac line does not require an additional lexical character at that point;
2. the same ASCII `J` extraction artifact occurs at another Syriac quotation boundary on the same page in Ramelli's Heb 2:12 discussion;
3. the independently known Peshitta calibration establishes the lexical kingdom word as `ܡܠܟܘܬܗ`;
4. an independent Syriac Luke commentary from the Syriac Orthodox Patriarchate likewise prints the Luke 17:21 base phrase with `ܡܠܟܘܬܗ ܕܐܠܗܐ`.

Classification:

`NONLEXICAL_LEGACY_FONT_OR_DIRECTIONAL_EXTRACTION_ARTIFACT`

The exact PDF-internal function of that artifact is not asserted.

## Independent Syriac control

The Syriac Orthodox Patriarchate's digital text of Bar Hebraeus's Luke commentary gives Luke 17:21 as:

`ܗܐ ܡܠܟܘܬܗ ܕܐܠܗܐ ܠܓܘ ܡܢܟܘܢ ܗܝ`

and then explicitly marks a Greek-aligned alternative:

`ܝܰܘܢܳܝܐ: ܒܓܘܟܘܢ ܐܝܬܝܗ`

Source:
`https://dss-syriacpatriarchate.org/.../ܟܪܘܙܘܬܐ-ܕܠܘܩܐ-ܡܣܒܪܢܐ/`

Evidence use:
- this independently corroborates `ܡܠܟܘܬܗ ܕܐܠܗܐ` in the Luke 17:21 Syriac context;
- it independently corroborates the exact target sequence `ܒܓܘܟܘܢ ܐܝܬܝܗ` as the Greek-aligned form;
- it is **not** treated as an independent Harklean manuscript witness or as proof of the entire Harklean line.

## Stable project encoding

Bound Harklean published-edition line:

`ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܒܓܘܟܘܢ ܐܝܬܝܗ`

Evidence class:

`DIRECT_RENDERED_SCHOLARLY_PAGE_READBACK_PLUS_CALIBRATED_LEGACY_FONT_DECODE_PLUS_INDEPENDENT_TARGET_CONTROL`

## Claim ceiling

Established:
- stable Unicode encoding of the Harklean quotation as printed by Ramelli from Kiraz;
- exact target phrase `ܒܓܘܟܘܢ ܐܝܬܝܗ`;
- distinction between Old Syriac `ܒܝܢܬܟܘܢ`, Peshitta `ܠܓܘ ܡܢܟܘܢ`, and Harklean `ܒܓܘܟܘܢ`.

Not established:
- direct manuscript-image autopsy of Vat. Syr. 268;
- a fresh diplomatic transcription preserving all manuscript diacritics or critical signs;
- lexical certainty for Greek `ἐντὸς ὑμῶν`;
- that Ramelli's semantic conclusion must be accepted.

Ramelli's claim that Peshitta and Harklean favor an interior reading remains attributed scholarly analysis.