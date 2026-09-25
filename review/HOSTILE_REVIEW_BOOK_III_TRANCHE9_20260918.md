# Hostile Review — Book III Versional/Patristic Luke 11 — Tranche 9

Status: PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR

Original review target:
- 74be5c1578850d4a0cf58cf0e71131a8fdfddfb0

Repair target:
- dde50284ea7e4e63736d36408918b65715de2004

Scope:
- sources/VERSIONAL_PATRISTIC_LEDGER_BOOK_III.yaml
- WIT-CURETONIAN-SYRIAC / Luke 11:4
- VAR-LUKE-11-2-4-LORDS-PRAYER
- LORDS_PRAYER_V1.md
- Luke 11:4 Old Latin/Syriac/Vulgate/Sahidic/Origen evidence
- Luke 11:2 minority Holy-Spirit petition traditions
- versional/patristic debt narrowing

## HR-BIII-006 — Marcion Spirit request was conflated with the kingdom-substitution witness family
Severity: HIGH
Original state: FAIL_REPAIRABLE
Repair state: CLOSED

Problem:
The first pass grouped:
- Greek witnesses 162 and 700;
- Gregory of Nyssa;
- Maximus;
- Marcion testimony via Tertullian

under one generalized Holy-Spirit petition relation described as replacing the "kingdom petition / first petition sequence."

That formulation erased an important distinction.

Published studies report:
- the 162/700/Gregory/Maximus family as substituting a Holy-Spirit petition for the kingdom petition;
- Tertullian/Marcion evidence as supporting some Spirit request in place of Marcion's first petition;
- modern Marcion scholarship explicitly warns that older apparatus/reconstructions wrongly make Marcion look like the 700/Gregory kingdom-substitution family.

Risk:
Normalizing the traditions would make indirect evidence for a lost Gospel text look stronger and more exact than it is, and could create a fictive single variant.

Repair:
- created VP-LUKE11-2-SPIRIT-FOR-KINGDOM for the 162/700/Gregory/Maximus family;
- retained PAT-MARCION-LUKE11-SPIRIT-PETITION as indirect testimony to a lost text;
- explicitly prohibited use of the 162/700/Gregory/Maximus wording to fill Marcion's text;
- split the apparatus control into kingdom_substitution_family and marcion_family;
- rewrote LORDS_PRAYER_V1.md to explain the distinction;
- retained exact Marcionite wording as NOT_RECOVERABLE_WITH_CONFIDENCE.

Repair commits:
- 86bcef7218bc7707f7c81f5d44ba01ed3d0befbc
- c1321a3f0f0aaeb3f445ee9cc917fe3a06eb16a5
- a9c8cb7507d357ce627cae8479c5e8dfd4aa7b41

Debt-retyping commit:
- dde50284ea7e4e63736d36408918b65715de2004

## Versional/patristic checks at repair target

PASS:
- VERSIONAL_STREAM != PHYSICAL_MANUSCRIPT invariant is explicit;
- PATRISTIC_CITATION != GOSPEL_MANUSCRIPT invariant is explicit;
- INDIRECT_LOST_TEXT_TESTIMONY != EXTANT_TEXT invariant is explicit;
- Old Latin collective support is typed as a versional stream rather than a manuscript;
- Curetonian Syriac is both represented in the versional stream and physically bound to WIT-CURETONIAN-SYRIAC;
- Peshitta and Harklean remain stream-level evidence rather than invented physical nodes;
- Vulgate and Sahidic remain shorter-form versional streams;
- Origen remains a patristic citation/exegete and directly reflects a shorter Lukan prayer form in On Prayer;
- the 162/700/Gregory/Maximus Spirit family is separated from Marcion;
- Marcion exact wording remains unrecoverable with confidence;
- no claim is made that versional agreement proves the underlying Greek archetype;
- PR #1 remained OPEN / DRAFT / UNMERGED / MERGEABLE;
- no commit status checks were reported.

## Evidence ceiling preserved

This tranche establishes:
- broad early Christian transmission of both shorter and expanded Luke 11 prayer forms;
- versional evidence for the longer Luke 11:4 deliverance petition in Old Latin and multiple Syriac streams;
- versional/patristic evidence for the shorter Luke 11:4 ending in Vulgate, Sahidic, and Origen;
- a real minority Holy-Spirit petition tradition;
- a real but indirect Marcion Spirit-request testimony.

It does NOT establish:
- one original versional archetype;
- that Syriac/Latin/Coptic agreements are independent historical attestations of Yeshua;
- exact wording of Marcion's prayer;
- physical manuscript binding for minuscules 162 and 700;
- exact patristic manuscript chains for Gregory/Maximus;
- autoptic verification.

## Remaining debt

Retyped:
- VERSIONAL_PATRISTIC_EXPANSION_BEYOND_LUKE11
- LUKE11_SPIRIT_VARIANT_162_700_PATRISTIC_PHYSICAL_BINDING

Still open:
- IMAGE_AUTOPTIC_LEVEL_VERIFICATION
- LUKE11_2_OPENING_ADDRESS_AUTOPTIC_CONFIRMATION
- LUKE11_4_SINAITICUS_HAND_STATE_AUTOPTIC_CONFIRMATION
- BEZAE_LUKE6_IMAGE_APPARATUS_VERIFICATION
- THOMAS_101_LACUNA_AUTOPTIC_CONFIRMATION
- THOMAS_3_AND_26_CRITICAL_EDITION_LINE_COLLATION
- LUKE17_21_ENTOS_FULL_CORPUS_LEXICAL_REVIEW
- P46_1COR7_LEAF_LOCALIZATION

## Verdict

PASS_FOR_TRANCHE / AFTER_INLINE_REPAIR.

Exact repaired state:
- dde50284ea7e4e63736d36408918b65715de2004

No merge, manuscript promotion, or historical-authenticity claim is authorized.
