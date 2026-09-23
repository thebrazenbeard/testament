# Hostile Review — Books I–IV Historical Spine — Tranche 5

Status: FAIL_REPAIRABLE / TEXTUAL-VARIANT ENFORCEMENT LAYER

Review target:
- 135470ab33b05a24544f9c350dce06d4b438a0b9

## Scope

Test whether the new variant ledger actually constrains scene prose rather than merely documenting interesting textual facts.

## Findings

### HR-IIV-033 — Variant ledger is not yet wired into scene packets
Severity: HIGH
State: FAIL

Problem:
The ledger has stable variant IDs, but scene packets still mostly mention variants in prose rather than declaring machine-visible dependencies.

Risk:
A later prose/review workflow can read SCN-II-BAPTISM, SCN-II-FINAL-MEAL, SCN-II-CRUCIFIXION, SCN-IV-TOMB, SCN-I-BIRTH, or SCN-II-FAMILY without querying the corresponding variant object.

Required repair:
add explicit `variant_controls`/stable-ID references to every affected scene packet and the scene index.

### HR-IIV-034 — Textual-base policy's high-risk list is stale
Severity: MEDIUM
State: FAIL

Problem:
TEXTUAL_BASE_POLICY lists Luke 3:22, Luke 22:15–20, Mark 16 and the Lukan genealogy but does not yet list Mark 6:3 or Luke 23:34a, even though the new ledger correctly treats both as consequential.

Required repair:
make the policy point to the authoritative variant ledger and include the two new high-risk cases.

### HR-IIV-035 — Variant ledger metadata calls its creation parent a review head
Severity: LOW
State: FAIL

Problem:
`review_head` currently names the parent from which the ledger was created, not a head that reviewed the ledger.

Required repair:
rename the field to `creation_parent` so provenance type is not misrepresented.

### HR-IIV-036 — Luke 23:34a lacks exact local witness-node binding
Severity: HIGH
State: BLOCKING_PARTIAL

Problem:
The ledger correctly preserves the originality debate and current scholarship identifies important early omissions, but Testament has not yet created exact witness nodes for the relevant Greek/Latin evidence.

Known scholarly controls:
- Whitlark & Parsons, DOI 10.1017/S0028688506000117, argue the external evidence favors omission.
- Nathan Eubank, DOI 10.2307/25765950, argues defenders of omission overstate the case and defends originality using external/intrinsic/patristic evidence.
- Oxford's *Latin New Testament* confirms omission of Luke 23:34 in part of the Old Latin tradition.

Required repair:
do **not** fake autoptic/exact apparatus work. Mark the variant `EXACT_WITNESS_BINDING_PENDING` and block quotation as settled Luke wording until exact witness nodes are added.

### HR-IIV-037 — Mark 6:3 upstream witness dependency must stay upstream-bound
Severity: MEDIUM
State: PASS_WITH_GUARD

Problem tested:
Could Testament silently promote On-Theo's pending P45 witness record?

Result:
No. The ledger labels the P45 note as upstream/pending and does not invent a local physical-witness record.

Guard remains:
do not materialize WIT-P45-MARK-6-3 locally until the upstream record/source evidence is reviewed or independently rebuilt.

## Verdict

FAIL_REPAIRABLE.

HR-IIV-033..035 require immediate structural repair.
HR-IIV-036 remains a deliberate blocking partial until exact witness work is performed.
HR-IIV-037 passes with its existing guard.

A tranche can pass after repair while still carrying a declared unresolved textual-research frontier; PASS means the uncertainty is correctly governed, not that the reading is solved.
