# Hostile Review — Book III Codex Sinaiticus Luke 11 Direct Transcription — Tranche 11

Status: PASS_FOR_TRANCHE / AFTER_CONFIDENCE_DOWNGRADE

Original review target:
- e4f898f9f4b9512b2ca314f2422cdce65ca9757b

Repair target:
- 17ebc85ae2ba411f79e258a23c57523ef666b94a

Scope:
- WIT-01-CODEX-SINAITICUS / Luke 11:2-4
- VAR-LUKE-11-2-4-LORDS-PRAYER
- LORDS_PRAYER_V1.md
- official Codex Sinaiticus electronic transcription at BL folio 236b
- Sinaiticus correction-state debt

## HR-BIII-007 — Overconfident Sinaiticus Luke 11:4 hand sequence

Severity: HIGH
Original state: FAIL_REPAIRABLE
Repair state: CLOSED_BY_DOWNGRADE_TO_CONFLICT

Problem:
Testament previously asserted a specific Sinaiticus hand sequence for the Luke 11:4 deliverance petition:
- original inclusion;
- first-corrector doubt;
- later removal of that doubt.

Fresh direct-source work exposed incompatible evidence.

The official Codex Sinaiticus Project page:
- localizes Luke 10:21-11:6 to British Library folio 236b, scribe A;
- visibly transcribes Luke 11:2 with simple Father;
- visibly includes the Matthean-style will petition;
- visibly ends Luke 11:4 after the testing petition in the plain extracted transcription.

Published NET apparatus meanwhile reports:
- longer deliverance reading: Sinaiticus corrector 1;
- shorter reading: Sinaiticus original hand and corrector 2.

That apparatus assignment conflicts with the precise hand chronology previously stored in Testament and with some older secondary summaries.

Risk:
The old control transformed a disputed correction history into machine-readable fact.

Repair:
- withdrew the asserted hand sequence from WIT-01-CODEX-SINAITICUS;
- added exact manuscript locator BL folio 236b;
- promoted the simple Father opening to DIRECT_ELECTRONIC_TRANSCRIPTION support;
- added direct electronic-transcription support for the expanded will petition in Sinaiticus;
- typed Luke 11:4 as CORRECTION_STATE_CONFLICT_DIRECT_POPUP_READBACK_REQUIRED;
- recorded the visible shorter electronic transcription separately from the correction-layer apparatus;
- withdrew the false hand sequence from VAR-LUKE-11-2-4-LORDS-PRAYER;
- rewrote LORDS_PRAYER_V1.md to state the conflict explicitly;
- retyped debt to direct image/correction-popup readback.

Repair commits:
- 78fd01aa68e0ba8cc17c1b59b9e0c010ff907c02
- a25ff8ad5f51b5c2367b1ab1199837b498c538b4
- 1b803fe5df7012d930d9019b44f4c64abc8eec76
- 17ebc85ae2ba411f79e258a23c57523ef666b94a

## Exact readback checks

PASS:
- Luke 11:2 opening address is bound to BL folio 236b;
- Sinaiticus opening address state is SHORTER_FATHER_ONLY_DIRECT_ELECTRONIC_TRANSCRIPTION;
- Sinaiticus will petition is EXPANDED_WILL_PETITION_DIRECT_ELECTRONIC_TRANSCRIPTION;
- Luke 11:4 state is CORRECTION_STATE_CONFLICT_DIRECT_POPUP_READBACK_REQUIRED;
- no BASE_TEXT_PRESENT_FIRST_CORRECTOR_DOUBTFUL_LATER_DOUBT_REMOVED state remains;
- no old hand-sequence prose remains in the variant ledger;
- the will-petition control now includes WIT-01-CODEX-SINAITICUS on the expanded side;
- the deliverance control carries Sinaiticus under correction_state_conflict rather than shorter/expanded normalization;
- LORDS_PRAYER_V1.md explicitly withdraws the prior chronology;
- remaining debts are:
  - LUKE11_2_SINAITICUS_DIRECT_IMAGE_READBACK
  - LUKE11_4_SINAITICUS_CORRECTION_POPUP_IMAGE_READBACK
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- no commit status checks were reported.

## Evidence ceiling preserved

This tranche establishes:
- exact official digital folio location for Luke 11:1-6;
- direct project-transcription support for simple Father;
- direct project-transcription support for the will petition;
- visible shorter Luke 11:4 plain transcription;
- a real conflict between plain transcription display and correction-layer/secondary descriptions.

It does NOT establish:
- exact original/corrector chronology at Luke 11:4;
- direct image-level Testament autopsy;
- which correction-layer encoding should control until the official popup/image is read directly;
- originality of the expanded or shorter prayer form.

## Verdict

PASS_FOR_TRANCHE / AFTER_CONFIDENCE_DOWNGRADE.

Exact repaired state:
- 17ebc85ae2ba411f79e258a23c57523ef666b94a

This pass improves reliability by lowering confidence where the evidence conflicts.

No merge, manuscript promotion, or historical-authenticity claim is authorized.
