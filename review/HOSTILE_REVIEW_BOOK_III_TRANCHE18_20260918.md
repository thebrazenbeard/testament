# Hostile Review — Book III Thomas Dependence Vocabulary Migration — Tranche 18

Status: PASS_FOR_TRANCHE / AFTER_CLASS_REPAIR

Original review target:
- fbc475324df5b177427211b909107079fa88561e

Repair target:
- a6664611a495f447288f95bdf94bcc35f2cfaaff

Scope:
- all Thomas-related Book III dependence/source-relation controls
- research/bibliography/THOMAS_SYNOPTIC_DEPENDENCE_V1.md controlled vocabulary
- migration of pre-matrix relation states

## HR-BIII-011 — Legacy Thomas relation states were not normalized to the new matrix vocabulary
Severity: MEDIUM
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
After introducing the source-level Thomas/Synoptic dependence matrix, most existing saying controls still carried older descriptive relation-state values, including:
- DISPUTED_INTERTEXTUAL_RELATION
- RELATED_TRADITION_DIRECTION_UNRESOLVED
- DISPUTED
- DISPUTED_WITH_CONFLATION_ARGUMENTS
- DISPUTED_SAYING_LEVEL_RELATION
- RELATED_KINGDOM_TRADITIONS_DIRECTION_UNRESOLVED

Only the newly repaired cross-bearing and wicked-tenants controls already used an allowed matrix state.

Risk:
The project would have a declared controlled vocabulary without actually enforcing it across legacy controls.

Repair:
- normalized nine legacy Thomas relation slots to RELATION_DISPUTED;
- preserved their prior descriptive meaning in evidence_balance fields;
- added bibliography links where appropriate;
- left Synoptic-only dependence states, intra-Thomas transmission states and semantic states untouched.

Repair commit:
- a6664611a495f447288f95bdf94bcc35f2cfaaff

## Validation

PASS:
All 11 Thomas-related Book III controls now expose at least one local Thomas/Synoptic relation slot using an allowed matrix value:
- VAR-BEATITUDES-POOR-MATT-LUKE-THOMAS
- VAR-ASK-SEEK-KNOCK-THOMAS-2-92
- VAR-SOWER-MUSTARD-THOMAS-9-20
- VAR-CAESAR-THOMAS-100
- VAR-LOST-SHEEP-THOMAS-107
- VAR-FIRST-LAST-THOMAS-4
- VAR-FAMILY-RENUNCIATION-THOMAS-55-101
- VAR-JUDGE-SPECK-THOMAS-26
- VAR-KINGDOM-WITHIN-THOMAS-3-113
- VAR-WICKED-TENANTS-THOMAS-65-66
- VAR-CROSS-DISCIPLESHIP-THOMAS-55

Allowed relation vocabulary remains:
- DIRECT_DEPENDENCE_STRONGLY_SUPPORTED
- SYNOPTIC_INFLUENCE_PROBABLE_DIRECTION_OR_MECHANISM_UNCERTAIN
- COMMON_TRADITION_PLAUSIBLE
- MIXED_OR_MULTISTAGE_TRANSMISSION_PLAUSIBLE
- RELATION_DISPUTED
- INSUFFICIENT_EVIDENCE

No relation slot in the audited Thomas set uses a value outside that set.

## Evidence ceiling preserved

This migration changes machine vocabulary, not historical conclusions.

It does NOT:
- strengthen any dependence claim;
- weaken any independence argument;
- convert disputed relations into direct dependence;
- erase cluster-specific nuance;
- alter witness evidence.

## Verdict

PASS_FOR_TRANCHE / AFTER_CLASS_REPAIR.

Exact repaired state:
- a6664611a495f447288f95bdf94bcc35f2cfaaff

Broader residual debt remains:
- THOMAS_SYNOPTIC_REDACTIONAL_FINGERPRINT_REVIEW

No merge, global Thomas-dependence verdict, or historical-authenticity claim is authorized.
