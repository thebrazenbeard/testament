# Hostile Review — Books I–IV Historical Spine — Tranche 6

Status: FAIL_REPAIRABLE / WITNESS-IDENTITY NORMALIZATION

Review target:
- 10e13d79c2b6751cf399305e99b0ba6d18851a8f

## HR-IIV-038 — Physical witnesses were given passage-scoped identities
Severity: HIGH
State: FAIL

Problem:
The registry contains:
- WIT-MARK-SINAITICUS-ENDING
- WIT-MARK-VATICANUS-ENDING

Those names identify a reading/use, not the physical manuscript.

This violates the inherited On-Theo invariant:
WITNESS = physical/recoverable witness identity;
passage/readings are locators beneath that witness.

Required repair:
replace them with general codex identities:
- WIT-01-CODEX-SINAITICUS
- WIT-03-CODEX-VATICANUS
and attach Mark 16 and other relevant readings as locators.

## HR-IIV-039 — Luke 23:34a blocking partial can now be materially reduced
Severity: HIGH
State: FAIL_REPAIRABLE

Current state:
VAR-LUKE-23-34A-FORGIVENESS correctly says exact witness binding pending.

New verified metadata / scholarly report basis:
- P75 / Hanna Papyrus 1 is an early-third-century Vatican manuscript of Luke/John.
- Vat. gr. 1209 / Codex Vaticanus is a fourth-century codex.
- Codex Bezae is Cambridge UL Nn.2.41, copied around 400 CE.
- Codex Washingtonianus / Freer Gospels is Smithsonian F1906.274, late fourth/early fifth century.
- Codex Koridethi is GA 038, ninth century.
- Eubank 2010 explicitly reports Luke 23:34a absent in P75, Vaticanus, first hand of Bezae, Koridethi, W and other/versional witnesses; he also documents early/diverse presence including Sinaiticus and patristic citations.

Required repair:
create physical witness nodes and bind the variant to them as SCHOLARLY_WITNESS_REPORT evidence.

Do not call this autoptic collation.

## HR-IIV-040 — Corrector state must not collapse into codex-level binary
Severity: HIGH
State: FAIL_REPAIRABLE

Problem:
At Luke 23:34a some codices have correction history. "Codex X includes/omits" can be false if hands differ.

Required repair:
record hand/state where scholarship distinguishes it, especially:
- Bezae first hand omission / later correction history;
- Sinaiticus base text/punctuation-correction history as reported.

Witness identity remains physical codex; hand-specific state belongs in locator metadata.

## HR-IIV-041 — Mark 16 variant links must survive witness normalization
Severity: MEDIUM
State: FAIL_REPAIRABLE

Required:
after renaming Sinaiticus/Vaticanus witness IDs, update VAR-MARK-16-ENDING and any scene/source references. No dangling IDs.

## Verdict

FAIL_REPAIRABLE.

This is a registry-schema integrity defect, not a dispute over theology. Normalize witness identity first, then rereview all references.
