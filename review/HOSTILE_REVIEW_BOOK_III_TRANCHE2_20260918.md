# Hostile Review — Book III Saying/Witness Controls — Tranche 2

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- 0e74e982cbd654252fc694575a74b710321fbd05

Repair target:
- 1937e11d764eb1e84b3c98dea2e50e18bee364bd

Scope added since tranche 1:
- VAR-JUDGE-SPECK-THOMAS-26
- VAR-KINGDOM-WITHIN-THOMAS-3-113
- VAR-WICKED-TENANTS-THOMAS-65-66
- WIT-POXY-1-GOSPEL-THOMAS
- Thomas 26 Greek/Coptic witness asymmetry
- Thomas 3 Greek/Coptic witness asymmetry
- Thomas 113 Coptic-only witness state
- Thomas 65/66 adjacent same-work arrangement
- JUDGE_MEASURE_SPECK_V1.md
- KINGDOM_WITHIN_AMONG_V1.md
- WICKED_TENANTS_V1.md

Review purpose:
- attack source/witness identity;
- attack Greek/Coptic witness asymmetry;
- find silent Coptic backfill into fragmentary Greek witnesses;
- find same-work counting errors;
- find theological/project preference leaking into evidence-layer translation;
- find dangling source, witness, or variant references.

## HR-BIII-003 — Luke 17:21 machine control silently narrowed the translation field
Severity: HIGH
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
KINGDOM_WITHIN_AMONG_V1.md preserved four documented interpretive possibilities for `entos hymon`:
- within you;
- among you;
- in your midst;
- less commonly, within your reach/power.

The newly created machine-readable control VAR-KINGDOM-WITHIN-THOMAS-3-113 listed only:
- within you;
- among you;
- in your midst.

The less-common reach/power option disappeared from the control layer.

Why this matters:
The Testament's authored theology has unusually strong incentive to privilege "within you." A control representation that silently narrows the option field can bias later prose even if the prose packet itself remains cautious.

Required repair:
- preserve the less-common reach/power interpretation in the machine-readable control;
- label it as less common rather than silently promoting it to equal consensus weight;
- keep the project-bias guard active.

Repair:
VAR-KINGDOM-WITHIN-THOMAS-3-113 now includes:
- live_options:
  - within you
  - among you
  - in your midst
- additional_attested_option:
  - within your reach/power
- an explicit note that this option is less common but remains in the documented interpretive field.

Repair commit:
- 1937e11d764eb1e84b3c98dea2e50e18bee364bd

## Mechanical hostile checks at repair target

PASS:
- every VAR-* ID referenced by SAYING_LEDGER_V1 resolves in VARIANT_LEDGER_BOOK_III_V1;
- no duplicate VAR-* IDs detected;
- every WIT-* reference in the Book III control ledger resolves in WITNESS_REGISTRY_V1;
- every SRC-* reference in the Book III control ledger resolves across APOCRYPHA_SOURCE_LEDGER.yaml + P0_SOURCE_LEDGER.yaml;
- all three newly matured packets advertise WITNESS_CONTROL_ACTIVE;
- WIT-POXY-1-GOSPEL-THOMAS is physically typed and passage-scoped rather than saying-scoped in identity;
- Thomas 26 Greek evidence remains explicitly fragmentary;
- Thomas 3 Greek evidence remains explicitly fragmentary/lacunose;
- Thomas 113 explicitly records no surviving Greek witness currently bound;
- Thomas 65/66 remain same-work adjacent forms, not independent historical witnesses;
- the kingdom project-bias guard is present in both control and packet;
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- no commit status checks were reported.

## Controls that held under hostile review

### Judge / measure / speck
- P.Oxy. I 1 gives direct fragmentary Greek evidence for Thomas 26.
- NHC II supplies the complete Coptic Thomas 26.
- Missing Greek wording is not silently filled from Coptic.
- The speck/log saying does not cause the whole Matthew/Luke cluster to be reconstructed as one original speech.
- "Judge not" is not reduced to a modern absolute ban on evaluation.

### Kingdom within / among
- Luke 17:21 remains a translation dispute.
- Thomas 3 is Greek + Coptic.
- Thomas 113 is Coptic-only in current witness coverage.
- Thomas does not settle Luke's Greek semantics.
- Book VIII's authored preference for "kingdom within" is explicitly prevented from functioning as Book III evidence.

### Wicked tenants
- Thomas 65 and 66 are adjacent but separate Coptic logia.
- Their adjacency is not converted into proof of historical independence or priority.
- Same-work adjacency is not counted as multiple independent attestation.
- Later supersessionist theology is explicitly blocked from becoming reconstructed historical speech.

## Remaining research debt

Still open:
- Luke 11:2 opening-address deeper witness binding;
- Luke 11:4 Sinaiticus hand/corrector normalization;
- versional and patristic witness expansion;
- image/autoptic-level verification;
- Thomas 101 lacuna edition/apparatus binding;
- deeper Thomas/Synoptic dependence bibliography where prose promotion depends on it;
- remaining unmatured Book III clusters;
- exact Greek/Coptic collation for Thomas 3 and Thomas 26 beyond current witness-scope controls;
- fuller lexical study of `entos` and its ancient usage before any prose claim of semantic preference.

## Verdict

PASS_FOR_TRANCHE.

Exact repaired source state:
- 1937e11d764eb1e84b3c98dea2e50e18bee364bd

This pass means the newly added Book III controls survived bounded hostile review after one concrete semantic-control defect was found and repaired.

It does not mean:
- Luke 17:21 has been translated definitively;
- Thomas dependence has been solved;
- historical authenticity has been proven;
- autoptic manuscript work is complete;
- remaining Book III clusters are mature;
- manuscript prose or merge is authorized.
