# Hostile Review — Book III Luke 17:21 Old Syriac + Harklean Text Encoding — Tranche 40

Status: PASS_FOR_TRANCHE / LUKE17_21_OLD_SYRIAC_HARKLEAN_TEXT_ENCODING_CLOSED

Review target:
- `93f19b1a0f93c5aa857e04b29cddf7da696e4106`

Scope:
- `research/collations/LUKE17_21_VERSIONAL_TEXT_COLLATION_V1.md`
- `research/audits/LUKE17_21_HARKLEAN_FONT_DECODE_V1.md`
- `sources/VERSIONAL_PATRISTIC_LEDGER_BOOK_III.yaml`
- `research/packets/KINGDOM_WITHIN_AMONG_V1.md`
- `LUKE17_21_OLD_SYRIAC_HARKLEAN_DIRECT_TEXT_ENCODING`

## Findings

No repairable evidence-layer defect found.

## Old Syriac checks

PASS:
- Curetonian and Sinaiticus Luke 17:21 CAL rows remain pinned to exact public-repository blobs;
- shared target `byntkwn` remains directly CAL-bound;
- `ܒܝܢܬܟܘܢ` remains explicitly typed as deterministic CAL-to-Syriac script conversion rather than source-native Unicode;
- the defective source Unicode verse field remains rejected rather than silently used;
- Old Syriac semantic ambiguity between interior/within and between/among remains preserved.

## Harklean source checks

PASS:
- Ramelli explicitly cites Kiraz, *Comparative Edition of the Syriac Gospels*, vol. 3, p. 352 for Luke 17:21b;
- Ramelli's rendered journal p. 264 directly reproduces the Harklean Syriac quotation;
- the Harklean quotation is bound as `ܗܐ ܓܝܪ ܡܠܟܘܬܗ ܕܐܠܗܐ ܒܓܘܟܘܢ ܐܝܬܝܗ`;
- target expression `ܒܓܘܟܘܢ` is distinct from Peshitta `ܠܓܘ ܡܢܟܘܢ` and Old Syriac `ܒܝܢܬܟܘܢ`;
- Ramelli's PDF legacy-font mojibake is not used directly as Unicode text.

## Decode checks

PASS:
- same-page Peshitta provides an independently bound calibration control for the legacy Syriac font;
- shared legacy glyph sequences map consistently across the Peshitta and Harklean quotations;
- a terminal ASCII `J` in PDF extraction is quarantined as nonlexical because the rendered line does not require it and the same artifact recurs at another Syriac quotation boundary on the page;
- no unknown `J` is silently promoted into a Syriac letter or manuscript sign;
- the Syriac Orthodox Patriarchate's Bar Hebraeus Luke commentary independently preserves `ܡܠܟܘܬܗ ܕܐܠܗܐ` and explicitly marks `ܒܓܘܟܘܢ ܐܝܬܝܗ` as Greek-aligned wording;
- that commentary is used only as an independent target/control, not as a second Harklean manuscript witness.

## Evidence-class checks

PASS:
- Harklean status is direct published-page readback plus calibrated legacy-font decode;
- no direct manuscript-image autopsy of Vat. Syr. 268 is claimed;
- no fresh diplomatic transcription with manuscript diacritics/critical signs is claimed;
- Ramelli's interior semantic interpretation remains attributed scholarship;
- Greek `entos hymon` remains unresolved at the project evidence layer.

## Repository checks

- PR #1 OPEN / DRAFT / UNMERGED / MERGEABLE;
- review target ahead of main: 384;
- review target behind main: 0;
- no commit statuses reported;
- no workflow runs reported.

## Debt disposition

Closed:
- `LUKE17_21_OLD_SYRIAC_HARKLEAN_DIRECT_TEXT_ENCODING`

Preserved broader work:
- Old Latin / other versional expansion remains under `VERSIONAL_PATRISTIC_MEDIUM_VALUE_TARGETED_EXPANSION`;
- manuscript-image autopsy is not required to call this text-encoding debt closed because the debt was direct stable text encoding, not manuscript-image verification.

## Verdict

`PASS_FOR_TRANCHE / LUKE17_21_OLD_SYRIAC_HARKLEAN_TEXT_ENCODING_CLOSED`

Exact reviewed state:
- `93f19b1a0f93c5aa857e04b29cddf7da696e4106`

No merge, publication, deployment, package installation, paid service, provider mutation, or other protected effect is authorized.