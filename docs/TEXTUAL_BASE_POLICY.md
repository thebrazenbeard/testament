# Textual Base and Witness Policy

Status: WORKING POLICY / REVIEW_REQUIRED

## Purpose

Testament cannot treat a verse reference as though one stable ancient wording simply exists behind every translation.

The project distinguishes:
1. WORK / SOURCE;
2. CRITICAL EDITION or scholarly reconstruction;
3. PHYSICAL / RECOVERABLE WITNESS;
4. CLAIM made from one or more of those objects.

This adopts the witness distinction developed upstream in On-Theo:
- docs/V1_WITNESS_MODEL_ADDENDUM.md
- registry/witnesses.yaml
- upstream cut: 7e354667770a6c4bed958a01c5ff843345a35b40

## Greek New Testament working base

For reproducible project work, Testament uses the **SBL Greek New Testament (SBLGNT)** as the default working Greek comparison text where a freely redistributable base is useful.

Reasons:
- critically edited Greek text;
- openly downloadable;
- CC BY 4.0 licensing;
- stable electronic formats.

Official project:
- https://www.sblgnt.com/
- https://www.sblgnt.com/license/

## Critical warning

SBLGNT is a working edition, not "the original New Testament."

Where wording materially affects a historical/theological conclusion, the project must also consult:
- current critical apparatus work;
- Editio Critica Maior where relevant/available;
- NA/UBS apparatus via licensed access or scholarly discussion;
- individual manuscript/version/patristic witnesses where the variant is consequential.

## Witness-specific rule

If a claim depends on a variant reading:
- cite source/work ID;
- cite witness ID when a specific manuscript/version matters;
- record access mode;
- separate witness date from composition date;
- never promote one witness reading to the whole work without textual-critical inference.

## Translation rule

No English translation governs historical conclusions by itself.

Testament prose may:
- make its own transparent translation;
- compare multiple scholarly translations;
- retain transliterated terms where English collapses an important ambiguity.

A literary translation choice belongs in apparatus when it narrows a contested semantic field.

## Hebrew Bible / Septuagint / Jewish texts

For scriptural intertexts:
- preserve Hebrew/Aramaic, Greek, and relevant DSS witness differences where consequential;
- consume On-Theo witness controls where already built;
- never let a later standardized form silently become the only first-century form.

## Authoritative variant control

Machine-readable control:
- apparatus/VARIANT_LEDGER_BOOKS_I_IV_V1.yaml

A scene with a listed variant must name the stable variant ID and satisfy its manuscript rule before prose promotion.

## Current high-risk New Testament variants already flagged

1. Luke 3:22 — baptismal voice; Codex Bezae/Old Latin Psalm 2:7-type reading versus the dominant critical-text form.
2. Luke 22:15–20 — multiple longer/shorter forms affecting the final-meal tradition.
3. Mark 16 ending — earliest attainable Markan text is currently judged by ECM scholarship to end at 16:8; later endings remain reception/canonical evidence but cannot be silently attributed to the earliest recoverable Markan form.
4. Lukan genealogy — manuscript formatting and transmission produce substantial variation across witnesses; genealogy comparison must not assume zero textual instability.
5. Mark 6:3 — "the carpenter, the son of Mary" versus an early alternative "son of the carpenter and Mary"; textual choice does not establish paternity stigma.
6. Luke 23:34a — the forgiveness prayer is absent from an important early textual stream but defended as original by other scholarship; exact local witness binding remains pending and the project treats the earliest reading as contested.

## Stop condition

If a scene's argument changes depending on one contested reading, the manuscript stops and the apparatus resolves or explicitly preserves the variant before prose promotion.
