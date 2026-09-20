# NEO Adapter Contract V1

Status: DESIGN READY / NOT INSTALLED / NO CANONICAL STATE CHANGE

External reference:
- repository: hughhowey/neo
- exact inspected head: a2846ff28f8bfec257565c6ca0ecce4c16242e61
- observed version: 0.7.5
- license: MIT

Testament authority:
- canonical manuscript/review/provenance state remains GitHub in this repository.
- NEO is an optional downstream authoring/reader surface only.

## Verified NEO storage contract

At the inspected NEO head, the Electron main process defines a book as a plain folder containing:
- `book.json`
- `chapters/*.html`
- `notes.html`
- `outline.html`
- `darlings.json`
- `stickies.json`

The default `book.json` created by NEO contains:
- `id`
- `title`
- `subtitle`
- `series`
- `author`
- `wordGoal`
- `created`
- `modified`
- `chapterOrder`
- `tabNames`

The renderer also supports `chapterTitles` keyed by chapter ID.

These observations are bound to NEO commit:
`a2846ff28f8bfec257565c6ca0ecce4c16242e61`

A future NEO head change reopens compatibility review.

## V1 direction

Only:

`Testament GitHub Markdown -> generated NEO book folder`

Not:

`NEO edits -> Testament GitHub`

The first version must be deterministic and non-destructive.

## Source surface

Initial reader source:
- `manuscript/draft_v1/PROLOGUE.md`
- `manuscript/draft_v1/BOOK_I_THE_WORLD.md`
- `manuscript/draft_v1/BOOK_II_YESHUA.md`
- `manuscript/draft_v1/BOOK_III_THE_SAYINGS.md`
- `manuscript/draft_v1/BOOK_IV_DEATH_AND_WHAT_FOLLOWED.md`
- `manuscript/draft_v1/BOOK_V_THE_MANY_CHRISTS.md`
- `manuscript/draft_v1/BOOK_VI_ECHOES.md`
- `manuscript/draft_v1/BOOK_VII_THE_KINGDOM_WITHIN.md`
- `manuscript/draft_v1/BOOK_VIII_THE_TESTAMENT_OF_THE_SPARK.md`

Excluded from the NEO prose surface by default:
- source ledgers;
- witness registries;
- hostile-review reports;
- machine-readable apparatus;
- ON_THEO evidence packets;
- internal continuation/exodus state.

Those remain available in GitHub and may later be rendered into a separate critical edition.

## Chapter mapping

Stable IDs are required. Do not use NEO's normal timestamp/random chapter IDs for generated content.

Recommended mapping:
- Prologue -> `ch-prologue`
- each Book section (`##`) -> `ch-bNN-sNN-<slug>`

Examples:
- `ch-b01-s01-under-other-mens-flags`
- `ch-b02-s13-the-cross`
- `ch-b08-s18-the-last-page`

`book.chapterOrder` follows `manuscript/CANON_ORDER.md`.

`book.chapterTitles` stores reader-facing section titles.

The Book identity is retained in the generated chapter title or outline so NEO's flat chapter model does not erase Testament's eight-book architecture.

## Generated book metadata

Recommended deterministic book ID:
- `book-testament-of-the-spark`

Recommended metadata:
- title: `The Testament of the Spark`
- author: authorial identity is NOT hard-coded until the project resolves the currently open first-person speaker/authorship decision.
- subtitle/series: blank unless Patrick sets them.
- wordGoal: 0 by default.
- created/modified: generated timestamps may be included, but must not be used as source-history authority.
- chapterOrder: deterministic.
- chapterTitles: deterministic.

The exporter must also emit a separate provenance receipt, not interpreted by NEO, containing:
- Testament repository;
- exact source commit;
- exact exporter version/commit;
- NEO compatibility commit;
- source file list;
- generated file hashes.

Suggested name:
- `TESTAMENT_NEO_EXPORT_RECEIPT.json`

## Markdown conversion

The adapter must preserve reader semantics, not source apparatus semantics.

Required V1 conversions:
- paragraphs -> `<p>`
- emphasis/strong -> equivalent inline HTML
- block quotations -> readable HTML block or paragraph form
- section breaks -> NEO's `<p class="scene-break">***</p>` only when the source explicitly represents a scene/section break
- ordinary headings inside a mapped chapter -> readable inline/subheading HTML
- HTML escaping before generated markup

Do not convert:
- Markdown comments or internal control metadata into factual reader claims;
- repository paths into prose unless deliberately included;
- unresolved apparatus debt into hidden confidence upgrades.

## Safety and provenance guards

1. NEO output is generated, disposable state.
2. Deleting a NEO export must never delete source Markdown.
3. NEO export success is not manuscript review PASS.
4. Editing generated HTML in NEO does not modify Testament.
5. Any future reverse-sync feature requires:
   - stable source anchors;
   - three-way reconciliation;
   - exact diff review;
   - preservation of source/provenance boundaries;
   - explicit user authorization before GitHub writes.
6. A reader-edition export must never silently include `FICTIONAL / LITERARY CONSTRUCTION` as upstream historical evidence.

## Installation boundary

V1 exporter should write to a caller-supplied output directory.

It must NOT:
- edit `~/Documents/NEO Library/library.json`;
- copy files into a user's NEO library automatically;
- launch NEO;
- overwrite an existing NEO book;
- delete prior exports.

An optional install/import step can be designed later after NEO-library mutation semantics are tested.

## Acceptance tests for a future exporter

At minimum:
1. same Testament commit -> byte-identical prose/chapter files, excluding explicitly timestamped receipt fields;
2. all expected source files represented;
3. stable chapter IDs/order across repeated runs;
4. no apparatus/source ledger files enter reader prose unexpectedly;
5. generated `book.json` parses as JSON and contains every chapter ID exactly once;
6. every `chapterOrder` ID has a corresponding `chapters/<id>.html`;
7. HTML is escaped and contains no raw Markdown heading markers;
8. source receipt records exact Testament and NEO commits;
9. exporter refuses to overwrite an existing output directory unless an explicit overwrite flag is supplied;
10. reverse sync remains absent in V1.

## Current conclusion

A Testament -> NEO adapter is technically low-friction because NEO's inspected format is plain-file and simple.

The difficult problem is not file conversion. It is preventing a convenient writing frontend from becoming an untracked second manuscript authority.

This contract resolves that by making V1 one-way and generated.
