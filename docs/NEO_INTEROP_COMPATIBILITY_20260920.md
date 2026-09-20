# NEO Interoperability Compatibility Pass — 2026-09-20

Status: STRUCTURAL_PASS / APPLICATION_OPEN_BLOCKED_BY_LIVE_LIBRARY_REGISTRATION / REVISED_PYTHON_SUITE_NOT_EXECUTED

## Exact state

Testament source:
- repository: `thebrazenbeard/testament`
- branch: `foundation/testament-v1`
- exact source commit: `3ff338187d716a56e39ffdc4780cd6d4651205e6`

NEO adapter work:
- branch: `docs/external-repository-candidates-v1-20260920`
- implementation head before this report: `a054eb3f98f9fce053a6f0baa0cae36d195d4a6f`

NEO compatibility target:
- repository: `hughhowey/neo`
- exact inspected commit: `a2846ff28f8bfec257565c6ca0ecce4c16242e61`

No merge, installation, live-library mutation, NEO launch, reverse sync, or canonical manuscript promotion occurred.

## Exact-head structural export result

A GitHub-connected structural pass applied the current adapter mapping rules to all nine Draft V1 prose files at the exact foundation commit.

Result:
- generated chapters: 103
- duplicate chapter IDs: 0
- empty generated chapter bodies: 0
- leaked `Status:` control lines: 0
- leaked raw H1/H2 Markdown markers: 0
- generated HTML characters: 80,578

The one generated book-level introduction is:
- `ch-b07-intro`
- title: `Book VII — The Kingdom Within — Introduction`
- content: `Nothing in this book is presented as recovered ancient teaching.`

The first Book VII IDs are therefore:
1. `ch-b07-intro`
2. `ch-b07-s01-the-problem-of-the-sky`
3. `ch-b07-s02-god-as-being`
4. `ch-b07-s03-god-as-ground`

## Defect found and repaired

The initial prototype stripped lines beginning with `Status:` and rejected any other prose before a Book's first `##` section.

That rule failed against the real Book VII file, which contains:
- a control line: `Status: EXPLICIT MODERN INTERPRETATION`
- a reader-facing disclaimer before section 1.

The first prototype would therefore refuse an exact-head export.

Repair:
- recognized `Status:` control lines remain excluded from reader output;
- remaining non-control book prelude is preserved as deterministic `ch-bNN-intro`;
- the Book VII disclaimer now survives in reader output without being attributed to section 1 or silently discarded.

Updated tests are persisted in `tests/test_export_testament_to_neo.py`.

The original local fixture suite passed 6/6 before this repair. The revised Python suite has not been executed in CI or an actual NEO runtime during this pass, so no post-repair Python PASS is claimed here.

## Pinned NEO loader contract

At NEO commit `a2846ff28f8bfec257565c6ca0ecce4c16242e61`:

1. Desktop NEO resolves its library under `Documents/NEO Library`.
2. `library.json` drives the bookshelf through `shelves[].bookIds`.
3. `readBookMeta(bookId)` resolves `<NEO Library>/<bookId>/book.json`.
4. `openBook(bookId)` iterates `book.chapterOrder` and reads `chapters/<chapterId>.html`.
5. `book.tabNames.notes` and `book.tabNames.outline` are accessed directly; the exporter supplies both.
6. `book.chapterTitles` is supported by the renderer.
7. A blank `book.author` is rendered as `Anonymous`.

The deterministic book ID `book-testament-of-the-spark` is technically usable because NEO does not require its normal timestamp/random ID pattern when reading an existing folder.

However, the installed folder name must equal the book ID, because NEO derives the path directly from `bookId`.

## Why a staged folder does not yet open in NEO

A valid generated folder outside `NEO Library` is not discoverable by NEO.

Even a valid folder copied into `NEO Library` remains absent from the bookshelf until the exact book ID is registered in a shelf's `bookIds` array.

NEO's built-in import route does not solve this while preserving the adapter contract:
- it accepts `.docx`, `.txt`, and `.md`;
- it creates a fresh NEO book;
- it generates new book/chapter IDs;
- it therefore does not preserve the deterministic identity/provenance mapping defined for Testament.

## Non-mutating install planner

Implemented:
- `tools/plan_neo_install.py`
- `tests/test_plan_neo_install.py`

The planner reads:
- a staged Testament NEO export;
- a real NEO `library.json`;
- an optional explicit shelf ID.

It validates:
- staged `book.json`;
- non-empty unique `chapterOrder`;
- presence of every chapter file;
- required NEO sidecars and Testament export receipt;
- target shelf existence;
- absence of an existing shelf registration;
- absence of an existing target book directory.

It then emits a plan containing:
- required target directory;
- exact shelf mutation;
- source/exporter/NEO provenance;
- explicit guards showing that nothing was applied.

It does not:
- copy any book files;
- edit `library.json`;
- launch NEO;
- enable reverse sync.

If author metadata is blank, the plan also warns that NEO will display `Anonymous`.

## Current conclusion

The Testament -> NEO format contract is structurally compatible with the pinned NEO loader after the Book VII prelude repair.

The remaining validation boundary is operational, not conceptual:

`exact staged export -> real library snapshot -> non-mutating install plan -> explicit authorization -> copy + shelf registration -> NEO launch -> application readback`

Until that final application-open sequence is performed, the status remains STRUCTURAL_PASS, not FULL_INTEROP_PASS.
