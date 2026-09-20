# NEO Adapter Contract V1

Status: PROTOTYPE IMPLEMENTED / EXACT-HEAD STRUCTURAL PASS / INSTALL PLANNER IMPLEMENTED / NOT INSTALLED / NO CANONICAL STATE CHANGE

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

## V1 implementation

Prototype implementation:
- `tools/export_testament_to_neo.py`
- `tests/test_export_testament_to_neo.py`
- `tools/plan_neo_install.py`
- `tests/test_plan_neo_install.py`

Current behavior:
- reads only the nine Draft V1 prose files declared in the adapter;
- creates stable chapter IDs and a deterministic chapter order;
- writes a caller-supplied NEO book folder;
- emits `book.json`, `chapters/*.html`, `notes.html`, `outline.html`, `darlings.json`, `stickies.json`, and `TESTAMENT_NEO_EXPORT_RECEIPT.json`;
- records exact caller-supplied Testament source and exporter commits plus the pinned NEO compatibility commit;
- leaves `author` blank by default while the authorial-speaker identity remains unresolved;
- refuses to overwrite an existing output directory unless `--overwrite` is explicit;
- contains no reverse-sync path and does not mutate a live NEO library.

Validation performed before persistence:
- local Python `unittest` suite: 6/6 PASS;
- current Draft V1 heading structure was checked across all nine prose files;
- the exact foundation source `3ff338187d716a56e39ffdc4780cd6d4651205e6` structurally maps to 103 generated chapters with zero duplicate IDs;
- Books VII and VIII contain leading `Status:` control lines; the exporter explicitly strips those from reader output;
- Book VII also contains a reader-facing pre-section disclaimer; exact-head verification exposed that the first prototype would reject the real manuscript, so V1 now preserves genuine book-level prelude as deterministic `ch-bNN-intro` chapters rather than dropping or misplacing it;
- the persisted GitHub files were read back after creation.

The original 6-test local fixture pass predates the exact-head prelude repair. Updated tests are persisted for the repaired behavior, but no claim is made here that the revised Python suite has executed in CI or inside NEO.

This is implementation evidence only. The exporter has not been installed into NEO, has not mutated `~/Documents/NEO Library`, and has not been validated by launching the NEO application.

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
- reader-facing Book prelude remaining after recognized control metadata is removed -> `ch-bNN-intro`
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

NEO's pinned application code establishes an additional registration requirement:

- desktop NEO resolves a book only as `<NEO Library>/<bookId>/book.json`;
- the bookshelf is driven by `library.json -> shelves[].bookIds`;
- `openBook(bookId)` then reads `book.json` and every `chapters/<chapterId>.html`;
- NEO's built-in manuscript importer accepts `.docx`, `.txt`, and `.md`, creates a new book, and generates new chapter IDs. That path therefore does not preserve this adapter's deterministic book/chapter identity.

Accordingly, a staged folder is structurally compatible but intentionally invisible to the NEO bookshelf until two controlled effects occur:
1. copy it into the NEO library under a folder whose name exactly equals `book.id`;
2. append that same `book.id` to an explicitly chosen shelf's `bookIds` array.

`tools/plan_neo_install.py` implements only the read-only planning phase. Given a staged export and a real `library.json`, it:
- validates the staged book and sidecars;
- verifies every chapterOrder ID has a corresponding chapter file;
- requires an explicit shelf when more than one exists;
- refuses an already registered book ID;
- refuses an existing target book directory;
- emits the exact target path and JSON shelf mutation;
- never copies files, edits `library.json`, launches NEO, or enables reverse sync.

Actual copy, library registration, and application launch remain outside this V1 planning step.

## Acceptance tests

The prototype now exercises the core contract with a bounded local suite. Remaining application-level interoperability still requires a real NEO import/open test before the adapter can be called operationally validated.

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

The prototype now enforces that boundary in code. The exact-head structural pass has also exposed and repaired the only current book-prelude mapping defect.

The next operational frontier is to run the staged exporter and install planner against an actual NEO library snapshot, inspect the generated plan, and only then—under separate explicit authorization—perform the copy + shelf registration and launch NEO for a true application-open/readback test.
