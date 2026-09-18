# Hostile Rereview — Books I–IV Tranche 5

Status: PASS_FOR_TRANCHE / TEXTUAL-RESEARCH DEBT PRESERVED

Original target:
- 135470ab33b05a24544f9c350dce06d4b438a0b9

Repair target:
- 9a30ab343cc8955541db11f87aa27c4b07337d41

## Result

### HR-IIV-033 — variant IDs wired into scenes
PASS.

All six affected scene packets now explicitly name their stable variant controls:
- SCN-I-BIRTH -> VAR-LUKE-3-23-38-GENEALOGY
- SCN-II-BAPTISM -> VAR-LUKE-3-22-BAPTISM-VOICE
- SCN-II-FAMILY -> VAR-MARK-6-3-MATRONYMIC
- SCN-II-FINAL-MEAL -> VAR-LUKE-22-15-20-FINAL-MEAL
- SCN-II-CRUCIFIXION -> VAR-LUKE-23-34A-FORGIVENESS
- SCN-IV-TOMB -> VAR-MARK-16-ENDING

### HR-IIV-034 — textual-base policy stale
PASS.

TEXTUAL_BASE_POLICY now points to the authoritative machine-readable variant ledger and includes Mark 6:3 and Luke 23:34a.

### HR-IIV-035 — provenance field mis-typed
PASS.

The ledger now uses `creation_parent`, not `review_head`.

### HR-IIV-036 — Luke 23:34a exact witness binding
PASS_AS_GOVERNED_PARTIAL.

The textual problem is not solved and is not claimed solved.

The ledger now explicitly states:
`witness_binding: EXACT_WITNESS_BINDING_PENDING`.

The crucifixion scene is linked to the variant and cannot treat the prayer as settled wording.

This is a passing governance state because the unresolved research is accurately represented and blocks overclaim.

### HR-IIV-037 — Mark 6:3 upstream witness dependency
PASS_WITH_GUARD.

The project continues to consume the On-Theo witness work as upstream-bound evidence and does not manufacture a local P45 autoptic claim.

## Tranche verdict

PASS_FOR_TRANCHE.

The next frontier is no longer "remember that textual variants exist."

It is exact witness/apparatus work on the remaining high-impact variants and then expansion of the same witness discipline into Book III sayings.
