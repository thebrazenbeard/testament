# Hostile Review — Book III Thomas/Synoptic Dependence Matrix — Tranche 16

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- 290c3a489fdd0b536a965549610ef893ae9be6d3

Repair target:
- 00af1423a5abe45b5b1b64a58ed3199c35fb731e

Scope:
- research/bibliography/THOMAS_SYNOPTIC_DEPENDENCE_V1.md
- SRC-GOSPEL-THOMAS source-level dependence control
- all Thomas-related Book III variant controls
- VAR-CROSS-DISCIPLESHIP-THOMAS-55 structural application audit
- Thomas-dependence debt narrowing

## HR-BIII-009 — Cross-bearing / Thomas 55 lacked an explicit local dependence state
Severity: MEDIUM
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
The new Thomas/Synoptic dependence matrix requires saying-level relation states rather than a global Thomas-dependent/independent assumption.

The application audit found that 10 Thomas-related Book III controls already exposed an explicit dependence/source-relation section.

VAR-CROSS-DISCIPLESHIP-THOMAS-55 did not.

Its prose correctly said Thomas 55 independence was not secure, but the machine-readable control lacked an explicit Thomas_vs_Synoptics state.

Risk:
A downstream consumer could infer uncertainty from prose inconsistently or skip dependence control entirely for this cluster.

Repair:
- added dependence_control to VAR-CROSS-DISCIPLESHIP-THOMAS-55;
- linked research/bibliography/THOMAS_SYNOPTIC_DEPENDENCE_V1.md;
- set Thomas_vs_Synoptics.state = RELATION_DISPUTED;
- preserved three live models:
  - DIRECT_OR_INDIRECT_SYNOPTIC_INFLUENCE
  - COMMON_TRADITION
  - MIXED_OR_MULTISTAGE_TRANSMISSION
- added same-source guard preventing Thomas 55 reuse from becoming duplicate independent attestation;
- retained historical plausibility/authenticity as a separate axis.

Repair commit:
- 5e0c07e3d1e73d92205694f09a3add2e69222904

Debt-retyping commit:
- 00af1423a5abe45b5b1b64a58ed3199c35fb731e

## Source-level matrix checks

PASS:
- research/bibliography/THOMAS_SYNOPTIC_DEPENDENCE_V1.md exists;
- Goodacre, Gathercole, Tuckett, Patterson, Kloppenborg and Sellew positions are represented as attributed scholarly models rather than project verdicts;
- evidence hierarchy prioritizes redactional fingerprints and extended non-formulaic agreement over short formulaic overlap;
- shorter Thomas form is explicitly not a chronology test;
- Thomas narrative absence is explicitly not proof of independence;
- Greek fragment evidence is required to be passage-specific;
- dependence and historicity are separate axes;
- global project states GLOBAL_THOMAS_INDEPENDENT and GLOBAL_THOMAS_DEPENDENT are disallowed except as descriptions of attributed models.

## Application checks

PASS:
All 11 current Thomas-related Book III variant controls now expose explicit local dependence/source-relation state:
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

No global dependence verdict silently determines those local states.

## Evidence ceiling preserved

This tranche does NOT establish:
- global Thomas independence;
- global Thomas dependence;
- direct copying for any cluster solely because parallels exist;
- independence solely because Thomas is shorter or lacks narrative context;
- historical authenticity from independence;
- historical worthlessness from dependence.

## Verdict

PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR.

Exact repaired state:
- 00af1423a5abe45b5b1b64a58ed3199c35fb731e

Residual debt:
- THOMAS_SYNOPTIC_REDACTIONAL_FINGERPRINT_REVIEW

No merge, manuscript promotion, or historical-authenticity claim is authorized.
