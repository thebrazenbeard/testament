# Hostile Review — Book III Exact Apparatus — Tranche 4

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- e5a38120d09057dc9ca6f466c89c594fb95f1bcc

Repair target:
- 6185f751f3e7cb5bd544b876f5d4169bdcdb22e0

Scope:
- Luke 11:2 opening-address witness binding
- Luke 11:4 deliverance-petition witness binding
- Codex Sinaiticus hand/corrector state at Luke 11:4
- LORDS_PRAYER_V1.md exact-apparatus deepening
- review/HOSTILE_REVIEW_BOOK_III_STATUS.yaml debt reconciliation

## HR-BIII-005 — Review status lagged exact-apparatus closure
Severity: MEDIUM
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
After the Lord's Prayer apparatus was deepened, the review status still listed:
- LUKE11_2_OPENING_ADDRESS_DEEPER_WITNESS_BINDING
- LUKE11_4_SINAITICUS_HAND_CORRECTOR_NORMALIZATION

as unresolved debt.

But the source state at the review target had already:
- bound Luke 11:2 opening address to named witnesses;
- bound Sinaiticus's Luke 11:4 hand/corrector sequence;
- updated the packet to distinguish published apparatus from autoptic verification.

Risk:
A stale status file could cause later work to redo completed witness-binding work or, worse, obscure the remaining boundary by mixing "published apparatus complete" with "autoptic confirmation still open."

Repair:
The two stale debt labels were replaced with:
- LUKE11_2_OPENING_ADDRESS_AUTOPTIC_CONFIRMATION
- LUKE11_4_SINAITICUS_HAND_STATE_AUTOPTIC_CONFIRMATION

This preserves the remaining evidence gap without pretending the named-witness work is unfinished.

Repair commit:
- 6185f751f3e7cb5bd544b876f5d4169bdcdb22e0

## Exact apparatus checks at repair target

PASS:
- P75 has Luke_11_2_opening_address = SHORTER_FATHER_ONLY;
- Sinaiticus has Luke_11_2_opening_address = SHORTER_FATHER_ONLY;
- Vaticanus has Luke_11_2_opening_address = SHORTER_FATHER_ONLY;
- Bezae has Luke_11_2_opening_address = EXPANDED_MATTHEAN_STYLE_ADDRESS;
- P75 has Luke_11_4_deliverance_petition = SHORTER_OMITS_DELIVERANCE;
- Vaticanus has Luke_11_4_deliverance_petition = SHORTER_OMITS_DELIVERANCE;
- Bezae has Luke_11_4_deliverance_petition = EXPANDED_DELIVERANCE_FORM;
- Sinaiticus has Luke_11_4_deliverance_petition = BASE_TEXT_PRESENT_FIRST_CORRECTOR_DOUBTFUL_LATER_DOUBT_REMOVED;
- VAR-LUKE-11-2-4-LORDS-PRAYER preserves Sinaiticus in a hand_state_complex bucket rather than forcing a binary present/absent classification;
- LORDS_PRAYER_V1.md distinguishes named-witness apparatus from autoptic collation;
- no commit status checks were reported.

## Evidence ceiling preserved

This tranche establishes:
- named witness support for the Luke 11:2 opening-address split;
- named witness support for Luke 11:4 shorter/expanded streams;
- published hand-state complexity for Sinaiticus.

It does NOT establish:
- autoptic image confirmation by Testament;
- an exact historical prayer;
- a globally original "short form";
- a solved Matthew/Luke/Didache source relation.

## Verdict

PASS_FOR_TRANCHE.

Exact repaired source state:
- 6185f751f3e7cb5bd544b876f5d4169bdcdb22e0

The former named-witness and hand-normalization debts are closed at the published-apparatus level and correctly retyped as autoptic-confirmation debt.

No merge, manuscript promotion, or historical-authenticity claim is authorized.
