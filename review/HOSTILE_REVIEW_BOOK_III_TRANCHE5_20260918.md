# Hostile Review — Book III Thomas 101 Lacuna Apparatus — Tranche 5

Status: PASS_FOR_TRANCHE / NO_REPAIR_REQUIRED

Review target:
- adab369f6f0de5407546bdd6565c8064721e1117

Scope:
- WIT-NHC-II-GOSPEL-THOMAS / Thomas_101
- VAR-FAMILY-RENUNCIATION-THOMAS-55-101
- FAMILY_RENUNCIATION_DISCIPLESHIP_V1.md
- HOSTILE_REVIEW_BOOK_III_STATUS.yaml debt retyping

Review purpose:
- prevent editorial restoration from becoming extant manuscript wording;
- distinguish short restored gaps from the larger unresolved mother-clause lacuna;
- verify that no Greek witness is silently implied for Thomas 101;
- verify that edition binding is not mislabeled as autoptic verification;
- verify that same-work Thomas 55/101 reuse remains non-independent.

## Findings

No new repairable defect found in this tranche.

The initial automated no-Greek probe returned false because the control places:
- greek_witness: NONE_SURVIVING_CURRENTLY_BOUND

at the parent Thomas-control scope rather than inside the nested Thomas_101 record.

Direct readback shows that this scope is unambiguous because:
- the parent guard covers both Thomas 55 and 101;
- fragment_scope_guard explicitly names logia 55 and 101;
- APOCRYPHA_SOURCE_LEDGER.yaml independently records Thomas_101 / greek: NONE_SURVIVING_CURRENTLY_BOUND.

This is not promoted to a defect merely to create a finding.

## Apparatus checks at review target

PASS:
- Thomas 101 remains EXTANT_COPTIC_WITH_LACUNAE;
- the witness node is bound to Bentley Layton's critical edition framework;
- Simon Gathercole is bound as commentary/lacuna control;
- short bracketed material is typed as editorial restoration;
- the larger mother-clause gap remains unresolved;
- neither restoration nor lacuna is promoted to direct manuscript wording;
- edition_state is EDITION_BOUND_AUTOPTIC_CONFIRMATION_PENDING;
- no currently bound Greek Thomas fragment is claimed for logion 101;
- Thomas 55/101 remain SAME_WORK_RELATED_FORMS_NOT_INDEPENDENT_WITNESSES;
- FAMILY_RENUNCIATION_DISCIPLESHIP_V1.md explicitly distinguishes edition-level closure from autoptic confirmation;
- review debt is retyped from THOMAS_101_LACUNA_EDITION_BINDING to THOMAS_101_LACUNA_AUTOPTIC_CONFIRMATION;
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- no commit status checks were reported.

## Evidence ceiling preserved

This tranche establishes:
- critical-edition-level control of Thomas 101's lacunose state;
- an explicit distinction between surviving text and editorial restoration;
- an explicit unresolved key gap in the mother clause.

It does NOT establish:
- autoptic manuscript confirmation by Testament;
- the missing wording of the mother clause;
- a recoverable Greek Thomas 101;
- Thomasine independence;
- a historically original form of the family-renunciation saying.

## Verdict

PASS_FOR_TRANCHE / NO_REPAIR_REQUIRED.

Exact reviewed source state:
- adab369f6f0de5407546bdd6565c8064721e1117

No source repair was needed after hostile review.

No merge, manuscript promotion, or historical-authenticity claim is authorized.
