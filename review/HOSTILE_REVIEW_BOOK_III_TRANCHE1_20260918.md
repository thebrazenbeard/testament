# Hostile Review — Book III Saying/Witness Controls — Tranche 1

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- 0fd7e1c2770fa43846485590b52dfa060150e473

Repair target:
- 82bbfa216371a8b9432a12b56a7ee064112f7bbf

Scope:
- apparatus/VARIANT_LEDGER_BOOK_III_V1.yaml
- sources/SAYING_LEDGER_V1.yaml
- sources/WITNESS_REGISTRY_V1.yaml
- sources/APOCRYPHA_SOURCE_LEDGER.yaml
- matured Book III packets for:
  - Lord's Prayer
  - enemy love / Didache
  - beatitudes / Thomas
  - ask / seek / knock
  - sower / mustard
  - Caesar / Thomas 100
  - lost sheep / Thomas 107
  - first / last / Thomas 4
  - family renunciation / Thomas 55/101

Review purpose:
- try to break source/witness identity;
- find stale or dangling controls;
- prevent dependent literary forms from masquerading as independent historical witnesses;
- prevent physical-witness date from becoming composition date;
- prevent Greek reconstruction from masquerading as extant text;
- prevent packet status from outrunning or lagging machine-readable control state.

## HR-BIII-001 — Lord's Prayer retained stale Didache 8.2 physical-witness debt
Severity: HIGH
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
The Lord's Prayer control still declared:
"Build a Didache 8.2 witness/source node rather than treating the work title as a physical witness."

Later Book III work had already created:
- SRC-DIDACHE;
- WIT-DIDACHE-H54-HIEROSOLYMITANUS.

But Didache 8.2 had never been attached as a locator to H, and the Lord's Prayer control had not been reconciled with the later source/witness state.

Risk:
A stale TODO could cause future prose/research to treat "Didache 8.2" as an untyped work-title witness even though the project had enough evidence to bind the physical manuscript.

Repair:
- added Didache_8_2 locator to WIT-DIDACHE-H54-HIEROSOLYMITANUS;
- bound VAR-LUKE-11-2-4-LORDS-PRAYER / Didache_8_2 to:
  - SRC-DIDACHE;
  - WIT-DIDACHE-H54-HIEROSOLYMITANUS;
- replaced stale build-node debt with deeper versional/patristic witness debt;
- updated LORDS_PRAYER_V1.md to record the physical binding.

Guard preserved:
H is dated to 1056 CE as a surviving witness. That date does not become the composition date of Didache or its prayer tradition.

Repair commits:
- 25450a839b0f7485f1013f68f69a90857c5fd0ac
- 2d86b2eead45b4b85b27da55a0ba8c5d36a77776
- 2431a4c6e764df743cb6f55a28b49523afab5d8e

## HR-BIII-002 — Lord's Prayer packet status lagged its control state
Severity: MEDIUM
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
LORDS_PRAYER_V1.md contained an active witness-control section and a machine-readable control, but its top-level status still read:
SAYING_PACKET / REVIEW_REQUIRED

Every later matured packet used:
SAYING_PACKET / WITNESS_CONTROL_ACTIVE / REVIEW_REQUIRED

Risk:
Packet-level status could mislead later tooling or reviewers into treating Lord's Prayer as less mature than the ledger state.

Repair:
- updated LORDS_PRAYER_V1.md status to WITNESS_CONTROL_ACTIVE / REVIEW_REQUIRED.

Repair commit:
- 82bbfa216371a8b9432a12b56a7ee064112f7bbf

## Mechanical hostile checks at repair target

PASS:
- every VAR-* control referenced by SAYING_LEDGER_V1 exists in VARIANT_LEDGER_BOOK_III_V1;
- no duplicate VAR-* IDs detected;
- every WIT-* reference used by the Book III variant ledger resolves in WITNESS_REGISTRY_V1;
- no stale "build a Didache 8.2 witness/source node" debt remains;
- Didache 8.2 resolves through SRC-DIDACHE to WIT-DIDACHE-H54-HIEROSOLYMITANUS;
- every matured packet in tranche scope advertises WITNESS_CONTROL_ACTIVE;
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- no commit status checks were reported.

## Controls that held under hostile review

- SOURCE != WITNESS != CLAIM remains intact.
- Multiple occurrences inside Gospel of Thomas do not become multiple independent historical witnesses.
- Matthew/Luke repetition is not automatically independent where literary dependence is probable.
- Thomas parallels are treated per saying, not by blanket independence/dependence.
- Coptic Thomas logia without Greek fragments are not described as extant Greek.
- Fragmentary Greek P.Oxy. 654 readings retain restoration/reconstruction guards.
- Physical witness date never becomes composition date.
- Shorter/compact/less-allegorized never automatically becomes earlier.
- Distinct endings and redactional settings are not harmonized into one recovered saying.

## Remaining research debt

This PASS does not close Book III.

Still open:
- LUKE11-2 opening-address variant needs deeper named-witness binding beyond edition signal;
- Sinaiticus hand/corrector state for Luke 11:4 remains unnormalized;
- versional and patristic witness expansion remains thin;
- image/autoptic-level verification is not complete;
- Thomas 101 lacunae need stronger edition/apparatus binding before detailed reconstruction;
- Thomas/Synoptic dependence arguments should be widened beyond the current comparison set where prose promotion depends on them;
- remaining Book III clusters are not yet matured to this witness-control depth;
- no sustained canonical prose promotion is authorized by this review.

## Verdict

PASS_FOR_TRANCHE.

This means the exact repaired source state at:
82bbfa216371a8b9432a12b56a7ee064112f7bbf

survived this bounded hostile review after two concrete defects were found and repaired.

It does not mean:
- historical truth is proven;
- every Book III cluster is mature;
- autoptic verification is complete;
- manuscript prose is authorized;
- merge is authorized.
