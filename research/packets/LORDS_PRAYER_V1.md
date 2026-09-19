# Lord's Prayer V1

Status: SAYING_PACKET / WITNESS_CONTROL_ACTIVE / REVIEW_REQUIRED

## Extant forms

Primary forms:
- Matthew 6:9–13;
- Luke 11:2–4;
- Didache 8.2.

Matthew and Luke preserve a recognizable common sequence while differing in length and wording. The Didache preserves a form close in important respects to Matthew and adds liturgical framing.

## Synoptic-source control

Under the Two-Source hypothesis, Matthew and Luke commonly derive their shared non-Markan prayer material from Q.

That is not the only live explanation.

A 2020 source-critical analysis by Olegs Andrejevs reopens whether the Lord's Prayer circulated through multiple autonomous liturgical recensions rather than exclusively through Q and explicitly compares Q and Farrer-type solutions.

Reference:
- Olegs Andrejevs, "A Source-Critical Analysis of the Lord's Prayer: Multiple Autonomous Recensions or Q?"
  DOI 10.2143/ETL.96.4.3288794

Therefore Testament records:
- shared early prayer tradition: strong;
- exact Q reconstruction: hypothesis-dependent;
- Didache independence from Matthew: disputed.

## Matthew / Luke differences

Matthew includes a fuller form:
- "our Father in heaven";
- "your will be done";
- fuller bread/debt/testing sequence;
- "debts" language.

Luke's shorter textual form is important, but wording varies across manuscript tradition and later harmonizing influence must be checked at witness level.

## Witness-control advance — Luke 11:2–4

Machine-readable control:
- `apparatus/VARIANT_LEDGER_BOOK_III_V1.yaml`
- variant ID: `VAR-LUKE-11-2-4-LORDS-PRAYER`

The current reproducible working text remains SBLGNT, which prints the shorter Lucan form and flags three Matthean-style expansions in the alternative tradition:
- an expanded heavenly address after "Father";
- the Matthean "your will be done" petition;
- the Matthean deliverance-from-evil petition after the testing petition.

Published apparatus summaries now bind the opening address directly: P75, Sinaiticus, and Vaticanus support simple "Father," while Bezae supports the expanded Matthean-style "Our Father in heaven." The will-petition control remains bound to P75/Vaticanus on the shorter side and Bezae on the expanded side. For the final deliverance petition, P75 and Vaticanus support omission while Bezae supports expansion.

Sinaiticus is now separately typed at Luke 11:4 rather than forced into a binary bucket. The exact original/corrector sequence is **not currently asserted**: published apparatus and older secondary summaries conflict, while the official default electronic transcription and correction layer are distinct display states.

This is enough to establish a deeper transmission control: Luke's prayer cannot be treated as textually flat, and later harmonization toward Matthew is strongly plausible in these locations. It is not enough to assign the Sinaiticus hand sequence without direct correction-layer evidence.

Didache 8.2 is now physically bound to `WIT-DIDACHE-H54-HIEROSOLYMITANUS`, the complete Greek Didache witness in Codex Hierosolymitanus 54. That closes the earlier untyped-work-title debt for this comparison. The codex is dated 1056 CE; that is the date of the surviving witness, not the composition date of Didache or of its prayer tradition.

It is not enough to establish:
- the exact historical wording spoken by Yeshua;
- a globally original "short form";
- a single literary route behind Matthew, Luke, and Didache;
- autoptic confirmation of the now-bound Sinaiticus hand-state at Luke 11:4.

Andrejevs 2020 remains the source-critical guard against pretending the literary problem is solved: Q, direct dependence, and multiple autonomous/liturgical recensions remain live explanatory models.

## Exact-apparatus deepening — opening address and Luke 11:4

The former opening-address debt is now materially reduced.

Current named-witness binding:
- P75: simple `Father`;
- Codex Sinaiticus: simple `Father`;
- Codex Vaticanus: simple `Father`;
- Codex Bezae: expanded `Our Father in heaven`.

### Direct Codex Sinaiticus electronic-transcription readback

Evidence-level clarification:

The Codex Sinaiticus Project describes its electronic transcription as a scholarly letter-by-letter transcription produced through independent transcription, comparison, and checking against the digital images. Its web edition links transcription and image at word level and separately represents corrections.

That makes the official transcription stronger than a generic secondary report, but it still is **not Testament image autopsy**.

The Project's XML specification adds an important control: correction alternatives are encoded as separate readings, and the web default is the first reading in the apparatus element; that is usually, but not invariably, the original reading. Therefore a default visible reading cannot by itself establish the corrector sequence.



The official Codex Sinaiticus Project page localizes Luke 10:21–11:6 to:
- British Library;
- folio 236b;
- scribe A.

Its visible electronic transcription directly confirms:
- Luke 11:2 opens with simple `Father`;
- Sinaiticus includes the Matthean-style will petition in Luke 11:2;
- the plain extracted transcription of Luke 11:4 ends after the testing petition, without visibly displaying the deliverance phrase.

That direct readback forced a correction to Testament's earlier hand-state claim.

The project had previously said:
- original inclusion;
- first-corrector doubt;
- later removal of doubt.

That sequence is now **withdrawn**.

The published NET apparatus instead assigns:
- longer deliverance form: Sinaiticus corrector 1;
- shorter form: Sinaiticus original hand and corrector 2.

Some older secondary summaries describe a different sequence.

Therefore current Sinaiticus state at Luke 11:4 is:

**CORRECTION-STATE CONFLICT / DIRECT CORRECTION-POPUP OR LOCUS-SPECIFIC XML APPARATUS READBACK REQUIRED; IMAGE READBACK REMAINS SEPARATE.**

The plain transcription and correction apparatus are different display layers.
Testament will not infer exact corrector chronology from the plain text alone.

At Luke 11:4 the secure current comparison is:
- P75: omits the deliverance petition;
- Vaticanus: omits it;
- Bezae: includes it;
- Sinaiticus: visible electronic transcription is shorter, while correction-layer chronology remains unresolved.

This improves the apparatus while lowering one overconfident claim rather than raising confidence artificially.

References:
- Codex Sinaiticus Project, BL folio 236b, Luke 10:21–11:6.
- Codex Sinaiticus Project, electronic-transcription methodology and web-edition documentation.
- Codex Sinaiticus Project, XML transcription specification for correction/readings encoding.
- NET Bible textual apparatus, Luke 11:4.

## Versional and patristic expansion — Luke 11

Machine-readable control:
- `sources/VERSIONAL_PATRISTIC_LEDGER_BOOK_III.yaml`

The Greek apparatus is not the whole transmission history.

### Luke 11:4 — expanded ending

Published textual apparatus reports the Matthean-style deliverance petition in:
- Old Latin collective witnesses (`it`);
- Curetonian Syriac (`sy-c`);
- Peshitta Syriac (`sy-p`);
- Harklean Syriac (`sy-h`).

The Curetonian reading is now additionally bound to the physical manuscript node:
- `WIT-CURETONIAN-SYRIAC`
- British Library Add MS 14451.

This does not mean the Syriac witnesses preserve the original Greek.
They are versional evidence and may reflect translation history, harmonization, or inherited Greek exemplars.

### Luke 11:4 — shorter ending

Published apparatus reports the shorter ending in:
- Vulgate (`vg`);
- Sahidic Coptic (`sa`);
- Origen.

Origen is especially useful because *On Prayer* explicitly compares Matthew and Luke and quotes a shorter Lukan prayer ending after the testing petition.

Origen is a patristic citation/exegete, not a Gospel manuscript.

His testimony can support textual history without becoming a physical Greek witness.

### Luke 11:2 — related but non-identical Holy-Spirit petition traditions

The first pass grouped two evidence problems too tightly.

They are now separated.

#### Kingdom-substitution family

Published scholarship reports a minority tradition in which the kingdom petition is replaced by a Holy-Spirit petition.

The two Greek manuscripts are now physically bound:

- `WIT-162-BARB-GR-449`
  - Vatican Apostolic Library `Barb.gr.449`;
  - dated by colophon to 13 May 1153;
  - Luke occupies ff. 119r–187v;
  - scholarly passage locator: folio 151.

- `WIT-700-EGERTON-2610`
  - British Library `Egerton MS 2610`;
  - 11th century;
  - Luke occupies ff. 145r–229v;
  - scholarly passage locator: folio 184.

Gregory of Nyssa and Maximus are patristic citation evidence rather than manuscript identities.

Gregory's evidence is now directly bound from his Greek *De oratione dominica*:
- dedicated control: `research/collations/LUKE11_2_GREGORY_NYSSA_SPIRIT_PETITION_V1.md`;
- in the third homily Gregory explicitly says Luke interprets the kingdom petition more clearly and that, in that Gospel, instead of `Ἐλθέτω ἡ βασιλεία σου`, the Spirit petition occurs;
- his direct attributed form is `Ἐλθέτω τὸ ἅγιον πνεῦμά σου ἐφ’ ἡμᾶς καὶ καθαρισάτω ἡμᾶς`;
- he then states that what Luke calls Holy Spirit Matthew calls kingdom;
- near the homily's end Gregory reuses the petition with changed word order in his own sermonic prose; that later reuse is not counted as a second textual witness.

This upgrades Gregory from generic patristic support to direct primary-text testimony.

It does **not** make Gregory a physical Gospel manuscript, prove his form original to Luke, or close the image-collation debt for 162/700.

Maximus remains a separate patristic support item at published-report level until independently direct-bound.

The two Greek witnesses are **not textually identical**.

Metzger's critical commentary reports:
- 700 with the fuller form corresponding to "May your Holy Spirit come **upon us** and cleanse us";
- 162 with a different possessive word order and **without** the "upon us" phrase.

Therefore Testament no longer stores one normalized Greek string for the whole family.

### Image-route deepening — 162 / 700

Dedicated route control:
- `research/collations/LUKE11_SPIRIT_VARIANT_162_700_IMAGE_ROUTE_V1.md`

The former folio-level image debt is now substantially narrower.

For **162 / Barb.gr.449**:
- DigiVatLib's IIIF manifest resolves folio 151r as canvas `p0313`;
- folio 151v is canvas `p0314`;
- both exact JP2 image-service identifiers are bound in the witness registry;
- the earlier scholarly locator still does not establish which side contains Luke 11:2;
- current runtime tools resolve both institutional targets but do not supply manuscript pixels for reliable direct collation.

Therefore Testament does **not** guess recto versus verso from sequence position.

For **700 / Egerton MS 2610**:
- Hoskier's 1890 full collation explicitly identifies one of its two reproductions as **folio 184 verso**;
- Hoskier states that this folio contains **Luke 11:2-8**;
- the Hoskier volume is publicly digitized through Wikimedia Commons / Internet Archive;
- this closes the earlier side-unspecified locator problem for 700;
- the current runtime still has not obtained renderable manuscript pixels from that facsimile, so image-level wording is not freshly transcribed.

Metzger's published wording comparison remains the text control:
- 700 includes `ἐφ’ ἡμᾶς`;
- 162 omits that phrase and differs in possessive order.

Current state:

**same variant family / two physically identified late Greek witnesses / non-identical wording / exact image routes materially deepened / direct pixel collation still pending.**

The live debt `LUKE11_SPIRIT_VARIANT_162_700_DIRECT_IMAGE_COLLATION` therefore remains open.

#### Marcion family

Marcion's lost Gospel is relevant through Tertullian's indirect polemical testimony.

Dieter Roth's reassessment is a hard guard:
the evidence supports **some kind of Spirit request in place of Marcion's first petition**, but older reconstructions go too far when they simply give Marcion the same kingdom-substitution wording preserved in 700/Gregory.

Therefore Testament records:

**162/700/Gregory/Maximus kingdom-substitution family = real minority variant.  
Marcion Spirit-request testimony = real indirect evidence.  
Those two are not normalized into one reading.  
Exact Marcionite wording = not recoverable with confidence.**

This distinction matters because Marcion's first petition itself is textually uncertain; Roth notes that "hallowed be your name" is not attested for Marcion's reconstructed text.

The variant remains particularly tempting because Luke strongly emphasizes the Holy Spirit elsewhere.

That theological fit is not evidence of originality.

References:
- NET Bible textual note, Luke 11:4.
- Origen, *On Prayer*, Lord's Prayer exposition.
- Tertullian, *Against Marcion* IV.26.
- D. T. Roth, "The Text of the Lord's Prayer in Marcion's Gospel" and later NA28 reassessment.
- Gregory of Nyssa, *De oratione dominica*, third homily; direct synchronized Greek text, GNO VII/II 39.18-19 control.
- `research/collations/LUKE11_2_GREGORY_NYSSA_SPIRIT_PETITION_V1.md`.
- Bruce M. Metzger, textual commentary on Luke 11:2.
- Vatican Apostolic Library, DigiVatLib IIIF manifest for Barb.gr.449.
- H. C. Hoskier, *A Full Account and Collation of the Greek Cursive Codex Evangelium 604* (1890), facsimile note for fol. 184v.

### Transmission consequence

Versional and patristic evidence makes the history more—not less—complex.

It strengthens three claims:
- Matthean harmonization pressure was broad enough to cross linguistic traditions;
- the shorter Luke form also circulated widely and was known to Origen;
- alternative liturgical/theological petitions could enter the prayer tradition.

It does **not** yield one recoverable universal original recension.

## Debt / sin

Matthew uses debt language; Luke explicitly uses "sins" while retaining debtor language in the reciprocal clause.

Benjamin Wold's 2022 Qumran/wisdom study treats Matthean debt remission as meaningful within Jewish wisdom/economic tradition rather than as a merely abstract metaphor.

Reference:
- Benjamin Wold, "Debt Remission in the Matthean Lord's Prayer":
  DOI 10.1017/9781009305082.007

This strengthens a Testament rule:
forgiveness language should not automatically lose its material debt resonance.

## Kingdom

The prayer links:
- divine name;
- kingdom/reign;
- daily/future bread;
- debt/forgiveness;
- testing/evil.

It therefore functions as a compact map of themes central to Book III.

Oxford Bibliographies' 2024 update calls the Lord's Prayer a major source for historical-Jesus research and a summary of kingdom concerns.

Reference:
- John Yieh, "Lord's Prayer":
  https://doi.org/10.1093/obo/9780195393361-0138

## Historical ceiling

Strong:
- an early Jesus-associated communal prayer tradition lies behind Matthew/Luke;
- the prayer is deeply embedded in kingdom/father/dependence/forgiveness tradition.

Not secure without further argument:
- exact original wording;
- exact language spoken by Yeshua;
- whether the longer or shorter extant recension is globally earlier;
- exact literary route to Didache.

## Book III rule

Do not print one harmonized "original Lord's Prayer" and call it recovered.

Possible literary strategy:
show a reconstructed minimal core, followed by major early forms in the apparatus, with every reconstructed word marked as inference.
