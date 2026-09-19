# Hostile Review — Book III Thomas 65–66 Redactional Fingerprint — Tranche 17

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- 73d0ea301031965912d2eb9f4d08b55151755561

Repair target:
- a4a1e3c7d40ae58cf6531aa9211891fa44aa22de

Scope:
- VAR-WICKED-TENANTS-THOMAS-65-66
- WICKED_TENANTS_V1.md
- research/bibliography/THOMAS_SYNOPTIC_DEPENDENCE_V1.md
- local Thomas/Synoptic redactional-fingerprint method

## HR-BIII-010 — Local dependence state used a non-approved controlled value
Severity: MEDIUM
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
The first fingerprint-deepening pass set:
- Thomas_vs_Synoptics.state = MIXED_EVIDENCE_REDACTIONAL_FINGERPRINT_CONTESTED

and:
- local_adjudication.state = SYNOPTIC_INFLUENCE_PLAUSIBLE_REDACTIONAL_FINGERPRINT_NOT_DECISIVE

Those are useful descriptive phrases but are not values permitted by the source-level Thomas dependence matrix.

Risk:
The project would claim a controlled vocabulary while silently proliferating bespoke states, defeating deterministic review and later querying.

Repair:
- Thomas_vs_Synoptics.state -> RELATION_DISPUTED
- local_adjudication.state -> RELATION_DISPUTED
- descriptive evidence weighting moved into separate evidence_balance fields.

Repair commit:
- a4a1e3c7d40ae58cf6531aa9211891fa44aa22de

## Fingerprint checks

PASS:
- Gathercole's local Lukan-redaction argument is represented:
  - Mark/Matthew lack the relevant "perhaps" motif;
  - Luke has one;
  - Thomas 65 has two;
  - this is treated as a plausible expansion of a Lukan redactional feature, not as settled direct copying.
- the Thomas 65 -> 66 tenants/stone adjacency is treated as stronger evidence than generic thematic overlap;
- sequence agreement is not allowed to identify direction by itself;
- Kloppenborg/autonomy arguments remain represented as counterevidence;
- Lanier's survey preserves source-critical direction/original-form/authenticity as contested;
- Sellew's comparative-method guard remains active;
- simpler/shorter Thomas wording is not used as a chronology test;
- no global Thomas-dependence conclusion is inferred from this local case;
- historical authenticity remains separate from literary dependence.

## Local adjudication

Controlled state:
- RELATION_DISPUTED

Evidence balance:
- SYNOPTIC_INFLUENCE_PLAUSIBLE_REDACTIONAL_FINGERPRINT_LOCALLY_WEIGHTY

Bounded interpretation:
- the doubled "perhaps" and 65–66 sequence give Synoptic/Lukan influence arguments real local weight;
- Thomas's distinct narrative form and contested tradition history prevent promotion to direct-copying fact.

## Verdict

PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR.

Exact repaired state:
- a4a1e3c7d40ae58cf6531aa9211891fa44aa22de

Broader residual debt remains:
- THOMAS_SYNOPTIC_REDACTIONAL_FINGERPRINT_REVIEW

No merge, manuscript promotion, global Thomas-dependence verdict, or historical-authenticity claim is authorized.
