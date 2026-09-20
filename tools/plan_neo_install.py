#!/usr/bin/env python3
"""Plan a safe NEO library registration without mutating the live library.

This tool reads a staged Testament NEO export and a NEO library.json, validates
that the book can be registered safely, and emits a JSON install plan. It never
copies files and never edits library.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

PLAN_SCHEMA = "testament.neo_install_plan.v1"


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_staged_book(staged_dir: Path) -> dict:
    if not staged_dir.is_dir():
        raise FileNotFoundError(f"Staged book directory not found: {staged_dir}")

    book_path = staged_dir / "book.json"
    if not book_path.is_file():
        raise FileNotFoundError(f"Missing staged book metadata: {book_path}")

    book = read_json(book_path)
    book_id = str(book.get("id") or "").strip()
    if not book_id:
        raise ValueError("Staged book.json has no non-empty id.")

    order = book.get("chapterOrder")
    if not isinstance(order, list) or not order:
        raise ValueError("Staged book.json has no usable chapterOrder.")

    if len(order) != len(set(order)):
        raise ValueError("Staged book.json contains duplicate chapter IDs.")

    missing = [
        chapter_id
        for chapter_id in order
        if not (staged_dir / "chapters" / f"{chapter_id}.html").is_file()
    ]
    if missing:
        raise ValueError(
            "Staged export is missing chapter files for: " + ", ".join(missing)
        )

    required_sidecars = (
        "notes.html",
        "outline.html",
        "darlings.json",
        "stickies.json",
        "TESTAMENT_NEO_EXPORT_RECEIPT.json",
    )
    missing_sidecars = [
        name for name in required_sidecars if not (staged_dir / name).is_file()
    ]
    if missing_sidecars:
        raise ValueError(
            "Staged export is missing required sidecars: "
            + ", ".join(missing_sidecars)
        )

    return book


def choose_shelf(library: dict, shelf_id: str | None) -> dict:
    shelves = library.get("shelves")
    if not isinstance(shelves, list) or not shelves:
        raise ValueError("NEO library.json has no shelves.")

    if shelf_id:
        for shelf in shelves:
            if shelf.get("id") == shelf_id:
                return shelf
        raise ValueError(f"Requested shelf id not found: {shelf_id}")

    if len(shelves) != 1:
        raise ValueError(
            "NEO library has multiple shelves; pass --shelf-id explicitly."
        )
    return shelves[0]


def build_install_plan(
    *,
    staged_dir: Path,
    library_json: Path,
    shelf_id: str | None = None,
) -> dict:
    book = validate_staged_book(staged_dir)

    if not library_json.is_file():
        raise FileNotFoundError(f"NEO library.json not found: {library_json}")

    library = read_json(library_json)
    shelf = choose_shelf(library, shelf_id)

    book_id = book["id"]
    shelves = library.get("shelves", [])
    registered_on = [
        candidate.get("id")
        for candidate in shelves
        if book_id in (candidate.get("bookIds") or [])
    ]
    if registered_on:
        raise ValueError(
            f"Book id {book_id!r} is already registered on shelf(s): "
            + ", ".join(str(x) for x in registered_on)
        )

    target_dir = library_json.parent / book_id
    if target_dir.exists():
        raise FileExistsError(
            f"Target NEO book directory already exists: {target_dir}"
        )

    shelf_books = shelf.get("bookIds")
    if not isinstance(shelf_books, list):
        raise ValueError(
            f"Target shelf {shelf.get('id')!r} has no valid bookIds array."
        )

    receipt = read_json(staged_dir / "TESTAMENT_NEO_EXPORT_RECEIPT.json")

    return {
        "schema_version": PLAN_SCHEMA,
        "apply": False,
        "operation": "COPY_STAGED_BOOK_AND_REGISTER_SHELF",
        "book": {
            "id": book_id,
            "title": book.get("title") or "",
            "staged_directory": str(staged_dir),
            "required_target_directory_name": book_id,
            "target_directory": str(target_dir),
        },
        "library": {
            "library_json": str(library_json),
            "shelf_id": shelf.get("id"),
            "shelf_name": shelf.get("name"),
            "mutation": {
                "operation": "append",
                "json_path": f"$.shelves[id={shelf.get('id')}].bookIds",
                "value": book_id,
            },
        },
        "provenance": {
            "source_repository": receipt.get("source_repository"),
            "source_commit": receipt.get("source_commit"),
            "exporter_commit": receipt.get("exporter_commit"),
            "neo_compatibility_commit": receipt.get("neo_compatibility_commit"),
        },
        "guards": [
            "NO_FILES_COPIED",
            "NO_LIBRARY_JSON_MODIFIED",
            "NO_NEO_PROCESS_LAUNCHED",
            "NO_REVERSE_SYNC",
            "TARGET_FOLDER_NAME_MUST_EQUAL_BOOK_ID",
        ],
        "next_authorized_effects_if_approved": [
            f"copy staged directory contents to {target_dir}",
            (
                f"append {book_id!r} to shelf {shelf.get('id')!r} "
                "in library.json with atomic write"
            ),
            "launch NEO only after both writes verify",
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged-book-dir", type=Path, required=True)
    parser.add_argument("--library-json", type=Path, required=True)
    parser.add_argument("--shelf-id", default=None)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional file for the plan; stdout when omitted.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    plan = build_install_plan(
        staged_dir=args.staged_book_dir,
        library_json=args.library_json,
        shelf_id=args.shelf_id,
    )
    rendered = json.dumps(plan, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if args.output:
        if args.output.exists():
            raise FileExistsError(
                f"Refusing to overwrite existing plan file: {args.output}"
            )
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
