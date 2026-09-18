# Hostile Review — Book III Saying/Witness Controls — Tranche 3

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- a81563c1334394479c7ec37f207b1b59537ec6be

Repair target:
- 6311e3ec5348b763c50860f757cf93ba82d81e6a

Scope added since tranche 2:
- VAR-SABBATH-BEZAE-LUKE-6-5
- VAR-DIVORCE-PAUL-1COR-7-RECEPTION
- VAR-CROSS-DISCIPLESHIP-THOMAS-55
- VAR-DOUBLE-LOVE-TORAH-SUMMARY
- VAR-FORGIVENESS-DEBT-MATT-LUKE-DIDACHE
- WIT-P46-PAULINE-CODEX
- WIT-D05-CODEX-BEZAE / Sabbath-worker locator
- INT-DOUBLE-LOVE-DEUT6-LEV19
- SABBATH_CONTROVERSIES_V1.md
- DIVORCE_MARRIAGE_V1.md
- CROSS_DISCIPLESHIP_V1.md
- LOVE_GOD_NEIGHBOR_V1.md
- FORGIVENESS_DEBT_V1.md

Review purpose:
- attack exact manuscript placement and witness identity;
- prevent early reception from becoming a wording claim;
- prevent historical plausibility from becoming authenticity;
- prevent Torah reception from becoming supersessionist narrative;
- prevent debt/sin/forgiveness semantic fields from collapsing;
- verify that Book III saying maturation is actually complete.

## HR-BIII-004 — Bezae Sabbath-worker locator misstated placement
Severity: HIGH
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
The initial witness/control wording described the distinctive Bezae Sabbath-worker saying as occurring "after Luke 6:5."

Better textual descriptions place the addition immediately after Luke 6:4 in Bezae's sequence; the reading is conventionally referred to as Luke 6:5D. Describing it merely as "after Luke 6:5" risks confusing canonical verse numbering with Bezae's actual sequence.

Why this matters:
The Book III control exists specifically to keep a striking single-manuscript reading from being flattened into normal Luke. Imprecise placement metadata undermines the very textual distinction the control is meant to enforce.

Repair:
- renamed locator:
  - from Luke_6_5_Sabbath_worker_addition
  - to Luke_6_5D_Sabbath_worker_addition
- changed witness note to state that the addition occurs immediately after Luke 6:4 in Bezae's sequence;
- added explicit placement_note to the variant control;
- removed all stale references to the old locator.

Repair commits:
- 067ed8696b506ed296f18722d6beb29c3d6142ca
- 6311e3ec5348b763c50860f757cf93ba82d81e6a

## Mechanical hostile checks at repair target

PASS:
- Book III saying clusters with packets: 18
- Book III clusters lacking witness/control maturation: 0
- no duplicate VAR-* IDs;
- every VAR-* reference in SAYING_LEDGER_V1 resolves;
- every WIT-* reference in VARIANT_LEDGER_BOOK_III_V1 resolves;
- every SRC-* reference resolves across P0 + apocrypha source registries;
- every INT-* reference resolves in SCRIPTURAL_INTERTEXT_LEDGER.yaml;
- no stale Luke_6_5_Sabbath_worker_addition locator remains;
- WIT-D05-CODEX-BEZAE resolves the corrected Luke_6_5D locator;
- WIT-P46-PAULINE-CODEX is a physical codex node with 1 Corinthians 7:10-11 as a locator rather than a saying-specific witness identity;
- all five newly matured packets advertise WITNESS_CONTROL_ACTIVE;
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- no commit status checks were reported.

## Controls that held under hostile review

### Sabbath
- the Bezae Sabbath-worker saying is textually real;
- it remains a distinctive D05 reading, not ordinary critical Luke;
- textual reality does not become originality or historical authenticity;
- its thematic fit with Testament's agency thesis is explicitly non-evidentiary;
- Sabbath conflict remains intra-Jewish legal/moral interpretation.

### Divorce
- 1 Corinthians 7 is treated as earlier reception of a Lord-command;
- Paul is not treated as a manuscript witness to Mark/Matthew/Luke wording;
- P46 witness date remains separate from Paul's composition date;
- exception structure and gender differences among Gospel forms remain visible;
- ancient divorce restriction is not converted into an authored mandate to endure abuse.

### Cross-bearing
- availability of crucifixion imagery before Yeshua's death establishes plausibility, not authenticity;
- multiple Gospel placements do not become multiple historical occasions by counting;
- Thomas 55 remains one Thomas source even when reused in both family-renunciation and cross-bearing controls.

### Double love
- Deuteronomy 6 and Leviticus 19 remain prior Jewish scriptural sources;
- Christianity is not narrated as replacing Jewish law with love;
- Mark/Matthew/Luke framing differences remain literary/redactional evidence.

### Forgiveness / debt
- debt, sin, forgiveness, reconciliation, restored relationship, and non-retaliation remain distinct semantic fields;
- Matthew, Luke, and Didache prayer forms remain source-specific;
- Didache dependence remains unresolved;
- modern boundary/accountability synthesis stays in the authored layer.

## Completion status

Book III saying-cluster maturation:
- 18 / 18 packeted saying clusters now have explicit machine-readable control bindings.
- This closes the saying-cluster maturation backlog as a control-layer task.

This does NOT close Book III overall.

## Remaining research debt

Still open:
- exact Greek/Coptic collation deepening where early Thomas papyri overlap NHC II;
- Luke 11:2 opening-address named-witness binding;
- Luke 11:4 Sinaiticus hand/corrector normalization;
- versional and patristic witness expansion;
- image/autoptic-level verification;
- Thomas 101 lacuna edition/apparatus binding;
- fuller Thomas/Synoptic dependence bibliography;
- fuller lexical study of Luke 17:21 entos;
- P46 institutional/shelfmark metadata deepening;
- direct image/apparatus verification of the Bezae Luke 6 sequence;
- transition from cluster maturation to exact apparatus/autoptic review.

## Verdict

PASS_FOR_TRANCHE.

Exact repaired source state:
- 6311e3ec5348b763c50860f757cf93ba82d81e6a

This pass closes the bounded Book III saying-cluster maturation backlog at the control layer after one concrete textual-placement defect was found and repaired.

It does not mean:
- all historical questions are solved;
- all manuscript readings are autoptically verified;
- every source relation is settled;
- manuscript prose is authorized;
- merge is authorized.
