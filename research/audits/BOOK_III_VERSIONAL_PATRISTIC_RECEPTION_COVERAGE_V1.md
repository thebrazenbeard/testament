# Book III Versional / Patristic / Early-Christian Reception Coverage Audit V1

Status: ACTIVE / HIGH_VALUE_EXPANSION

Primary ledger:
- sources/VERSIONAL_PATRISTIC_LEDGER_BOOK_III.yaml

Purpose:
- replace the vague debt VERSIONAL_PATRISTIC_EXPANSION_BEYOND_LUKE11 with evidence-ranked coverage;
- distinguish versional translations, patristic exegesis, early-Christian reception texts, and indirect testimony to lost works;
- add ancient reception only where it materially constrains transmission, wording, or reception history.

## Type system

VERSIONAL_STREAM:
- translation tradition or version of a canonical passage;
- never automatically a physical Greek manuscript.

PATRISTIC_EXEGESIS:
- an ancient Christian author's interpretation or quotation;
- not a Gospel manuscript.

EARLY_CHRISTIAN_RECEPTION:
- a noncanonical early Christian work that reuses, parallels, or applies related Jesus tradition;
- not automatically dependent on a canonical Gospel;
- not automatically independent historical attestation.

INDIRECT_TESTIMONY_TO_LOST_TEXT:
- a surviving author reports or quotes a work no longer extant in that form;
- testimony is real evidence;
- the lost text is not thereby physically recovered.

NONCANONICAL_PARALLEL_TRADITION:
- related early Jesus/saying tradition outside the canonical Gospel forms;
- literary direction remains a separate question.

## Existing mature coverage

### Lord's Prayer / Luke 11
Status: SUBSTANTIAL
Controls:
- VP-LUKE11-4-LONGER-VERSIONAL-STREAMS
- VP-LUKE11-4-SHORTER-VERSIONAL-STREAMS
- PAT-ORIGEN-ON-PRAYER-LUKE11
- VP-LUKE11-2-SPIRIT-FOR-KINGDOM
- PAT-MARCION-LUKE11-SPIRIT-PETITION

### Kingdom location / Luke 17:21
Status: SUBSTANTIAL_PARTIAL_DIRECT
Controls:
- VP-LUKE17-21-LATIN-SYRIAC-RECEPTION
- PAT-TERTULLIAN-LUKE17-21-POWER
- research/collations/LUKE17_21_VERSIONAL_TEXT_COLLATION_V1.md

Residual:
- Old Syriac / Harklean direct stable text encoding.

### Enemy love / nonretaliation
Status: ANCIENT_PARALLEL_ALREADY_PRESENT_OUTSIDE_RECEPTION_LEDGER
Existing source:
- Didache 1.3-4
- WIT-DIDACHE-H54-HIEROSOLYMITANUS

Need:
- bind Didache 1.2-3 into this reception ledger so its double-love + enemy-love sequence can be queried consistently.

### Forgiveness / debt
Status: ANCIENT_PARALLEL_ALREADY_PRESENT_OUTSIDE_RECEPTION_LEDGER
Existing source:
- Didache 8.2 Lord's Prayer tradition via H54.

Need:
- no duplicate record merely to inflate coverage; reuse existing Didache/Lord's Prayer evidence where relevant.

## High-value immediate expansions

### Double love / Torah summary
Variant:
- VAR-DOUBLE-LOVE-TORAH-SUMMARY

Priority: HIGH

Ancient evidence:
- Didache 1.2 directly juxtaposes love of God and neighbor;
- Didache 1.3 immediately develops enemy-love/nonretaliation material.

Why it matters:
- confirms an early Christian reception pattern combining Torah-summary love language with Jesus-tradition ethical expansion;
- does not make the double command a Christian invention;
- does not identify literary direction by itself.

### Divorce / remarriage
Variant:
- VAR-DIVORCE-PAUL-1COR-7-RECEPTION

Priority: HIGH

Ancient evidence:
- Shepherd of Hermas, Mandate 4.

Why it matters:
- shows an early Christian reception/application trajectory for separation, adultery, repentance and remarriage;
- creates a reception bridge after Paul's early Lord-command evidence;
- must not be treated as a direct Gospel quotation or fifth Gospel witness.

### Seek / find
Variant:
- VAR-ASK-SEEK-KNOCK-THOMAS-2-92

Priority: HIGH

Ancient evidence:
- Clement of Alexandria, Stromata 2.9.45.5 and 5.14.96.3;
- testimony attributed to the Gospel according to the Hebrews.

Why it matters:
- independently preserves/report the seek -> find -> marvel -> reign -> rest chain strongly parallel to Greek Thomas 2;
- constrains the saying's wider early-Christian transmission;
- is indirect testimony to a lost/non-extant Gospel form, not a physical Gospel-of-the-Hebrews manuscript.

## Medium-value future candidates

- Beatitudes: ancient poverty/reversal reception where it clarifies Matt/Luke/Thomas relation.
- Cross-bearing / family renunciation: early reception only if a text constrains the saying combination rather than merely alluding to discipleship.
- Judge / measure / speck: early reception only if wording or cluster composition is informative.
- Caesar: early exegesis may illuminate interpretation, but should not be added merely as theological commentary.
- Lost sheep: noncanonical/patristic reuse may matter if it bears on distinctive endings.
- Wicked tenants: patristic allegory is abundant but often too late/redactional to constrain earliest form.
- Sabbath Bezae addition: patristic discussion is useful only if it directly witnesses or discusses the distinctive Bezae saying.
- First/last: short portable maxim makes reception easy to overcount.

## Low-value / avoid-by-default

Do not add:
- late homiletic paraphrases that merely repeat a canonical text;
- reception witnesses with no bearing on wording, transmission, dependence, or early interpretation;
- multiple Fathers repeating the same later ecclesial interpretation just to increase citation count.

## Completion rule for the broad debt

VERSIONAL_PATRISTIC_EXPANSION_BEYOND_LUKE11 may be narrowed when:
- the three HIGH priority expansions above are bound;
- the existing Didache evidence is queryable through the reception ledger;
- remaining clusters are explicitly triaged HIGH / MEDIUM / LOW rather than left as an undefined backlog.

It does NOT require one reception record per Book III cluster.

Future newly discovered high-value ancient evidence reopens the relevant local coverage automatically.
