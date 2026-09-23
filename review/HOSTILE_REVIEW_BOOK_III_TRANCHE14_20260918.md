# Hostile Review — Book III Luke 17:21 ENTOS Corpus Review — Tranche 14

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- dff069de3548a36e955b3f2055ba3056859596f3

Repair target:
- 9d8b435419100435fc67556c058294dd55cda624

Scope:
- research/lexicon/ENTOS_WITHIN_AMONG_V1.md
- VAR-KINGDOM-WITHIN-THOMAS-3-113
- KINGDOM_WITHIN_AMONG_V1.md
- LUKE17_21_ENTOS_FULL_CORPUS_LEXICAL_REVIEW debt transition

## HR-BIII-008 — Debt rename mutated historical tranche record instead of live frontier
Severity: MEDIUM
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
The first debt-narrowing write replaced the first occurrence of:
- LUKE17_21_ENTOS_FULL_CORPUS_LEXICAL_REVIEW

inside HOSTILE_REVIEW_BOOK_III_STATUS.yaml.

That first occurrence belonged to tranche_7.reviewed_debt, not remaining_debt.

Result:
- historical tranche 7 provenance was silently rewritten;
- the live remaining_debt entry stayed stale.

Risk:
Review history would no longer describe what tranche 7 actually reviewed, while the current frontier would falsely remain unresolved at the old level.

Repair:
- restored tranche_7.reviewed_debt to LUKE17_21_ENTOS_FULL_CORPUS_LEXICAL_REVIEW;
- changed only live remaining_debt to LUKE17_21_ENTOS_VERSIONAL_PATRISTIC_RECEPTION_BINDING.

Repair commit:
- 9d8b435419100435fc67556c058294dd55cda624

## Lexical/corpus checks at repair target

PASS:
- ENTOS_WITHIN_AMONG_V1.md is marked CORPUS_REVIEW_ADVANCED;
- lexical center is explicitly interiority / bounded inclusion;
- LSJ/classical extensions involving bounds, range, group position, self-control and power/reach are represented;
- papyrological breadth is acknowledged without treating word-index counts as contextual proof;
- Roberts's within-your-power argument remains SCHOLARLY_ARGUMENT / NOT PROJECT FACT;
- Holmén is recorded as a major semantic-restriction study without inventing a conclusion not directly available in the accessible source;
- Ramelli's broad Greek + Syriac argument for inside/within is represented as a substantive scholarly position, not project fact;
- the substantial modern commentary preference for among/in-your-midst is represented as largely contextual/exegetical rather than a bare dictionary conclusion;
- "among" is not declared lexically impossible;
- "within you" is not converted into individualized private spirituality by lexical force alone;
- "within reach/power" remains live as an attested semantic extension;
- the apparatus explicitly states LEXICON_ALONE_DOES_NOT_DECIDE_LUKE_17_21;
- the Book VIII project-bias guard remains active;
- historical tranche 7 provenance is preserved;
- live debt is narrowed to LUKE17_21_ENTOS_VERSIONAL_PATRISTIC_RECEPTION_BINDING;
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- branch remained 0 behind main;
- no commit status checks were reported.

## Corpus-level result

The bounded lexical result is:

1. interiority / bounded inclusion is the lexical center of entos;
2. among/in-your-midst remains contextually defensible, especially as a group-bounded construal;
3. within-your-reach/power remains an attested semantic extension;
4. the final Luke 17:21 translation cannot be decided by lexicon alone;
5. translation adjudication necessarily moves into syntax, discourse, versional/patristic reception and Lukan theology.

## Evidence ceiling preserved

This tranche does NOT establish:
- that Luke 17:21 certainly means within you;
- that Luke 17:21 certainly means among you;
- that within-your-power is the intended idiom;
- that lexical interiority proves Testament's agency thesis;
- that modern commentary preference can be re-described as lexical certainty.

## Verdict

PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR.

Exact repaired state:
- 9d8b435419100435fc67556c058294dd55cda624

Residual debt:
- LUKE17_21_ENTOS_VERSIONAL_PATRISTIC_RECEPTION_BINDING

No merge, manuscript promotion, or theological-preference promotion is authorized.
