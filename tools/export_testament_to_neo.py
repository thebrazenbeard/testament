#!/usr/bin/env python3
"""Deterministic one-way Testament Markdown -> NEO book exporter.

Canonical manuscript state remains GitHub Markdown. Generated NEO output is disposable.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

TESTAMENT_REPOSITORY = "thebrazenbeard/testament"
NEO_COMPATIBILITY_COMMIT = "a2846ff28f8bfec257565c6ca0ecce4c16242e61"
EXPORTER_VERSION = 1
BOOK_ID = "book-testament-of-the-spark"
BOOK_TITLE = "The Testament of the Spark"

SOURCE_FILES = (
    ("PROLOGUE.md", None),
    ("BOOK_I_THE_WORLD.md", 1),
    ("BOOK_II_YESHUA.md", 2),
    ("BOOK_III_THE_SAYINGS.md", 3),
    ("BOOK_IV_DEATH_AND_WHAT_FOLLOWED.md", 4),
    ("BOOK_V_THE_MANY_CHRISTS.md", 5),
    ("BOOK_VI_ECHOES.md", 6),
    ("BOOK_VII_THE_KINGDOM_WITHIN.md", 7),
    ("BOOK_VIII_THE_TESTAMENT_OF_THE_SPARK.md", 8),
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
SECTION_RE = re.compile(r"^##\s+(?:(\d+)\.\s*)?(.+?)\s*$")
SCENE_BREAK_RE = re.compile(r"^\s*(?:\*{3,}|-{3,}|_{3,})\s*$")
UL_RE = re.compile(r"^\s*[-+*]\s+(.+)$")
OL_RE = re.compile(r"^\s*\d+[.)]\s+(.+)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
STRONG_RE = re.compile(r"\*\*([^*]+)\*\*|__([^_]+)__")
EM_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)|(?<!_)_([^_\n]+)_(?!_)")
CODE_RE = re.compile(r"`([^`\n]+)`")


@dataclass(frozen=True)
class Chapter:
    chapter_id: str
    title: str
    source_file: str
    body_markdown: str


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    ascii_text = re.sub(r"['’]", "", ascii_text)
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    return ascii_text or "untitled"


def strip_numeric_prefix(title: str) -> str:
    return re.sub(r"^\s*\d+\.\s*", "", title).strip()


def _format_inline_segment(text: str) -> str:
    escaped = html.escape(text, quote=True)
    escaped = CODE_RE.sub(lambda m: f"<code>{m.group(1)}</code>", escaped)
    escaped = STRONG_RE.sub(
        lambda m: f"<strong>{m.group(1) or m.group(2)}</strong>", escaped
    )
    escaped = EM_RE.sub(
        lambda m: f"<em>{m.group(1) or m.group(2)}</em>", escaped
    )
    return escaped


def _inline(text: str) -> str:
    # Parse links before formatting so emphasis regexes never touch generated HTML
    # attributes or URL characters.
    parts: list[str] = []
    last = 0
    for match in LINK_RE.finditer(text):
        parts.append(_format_inline_segment(text[last:match.start()]))
        label = _format_inline_segment(match.group(1))
        href = html.escape(match.group(2), quote=True)
        parts.append(f'<a href="{href}">{label}</a>')
        last = match.end()
    parts.append(_format_inline_segment(text[last:]))
    return "".join(parts)


def markdown_to_html(markdown: str) -> str:
    """Convert the bounded Markdown subset used by Draft V1 into NEO-safe HTML."""
    lines = markdown.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    blockquote: list[str] = []
    list_mode: str | None = None
    list_items: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{_inline(' '.join(x.strip() for x in paragraph))}</p>")
            paragraph = []

    def flush_quote() -> None:
        nonlocal blockquote
        if blockquote:
            text = " ".join(x.strip() for x in blockquote)
            out.append(f"<blockquote><p>{_inline(text)}</p></blockquote>")
            blockquote = []

    def flush_list() -> None:
        nonlocal list_mode, list_items
        if list_mode and list_items:
            tag = "ul" if list_mode == "ul" else "ol"
            rendered = "".join(f"<li>{_inline(item)}</li>" for item in list_items)
            out.append(f"<{tag}>{rendered}</{tag}>")
        list_mode = None
        list_items = []

    def flush_all() -> None:
        flush_paragraph()
        flush_quote()
        flush_list()

    for raw in lines:
        line = raw.rstrip()

        if not line.strip():
            flush_all()
            continue

        if SCENE_BREAK_RE.match(line):
            flush_all()
            out.append('<p class="scene-break">***</p>')
            continue

        heading = HEADING_RE.match(line)
        if heading:
            flush_all()
            level = min(len(heading.group(1)) + 1, 6)
            out.append(f"<h{level}>{_inline(heading.group(2).strip())}</h{level}>")
            continue

        if line.lstrip().startswith(">"):
            flush_paragraph()
            flush_list()
            blockquote.append(line.lstrip()[1:].lstrip())
            continue
        elif blockquote:
            flush_quote()

        ul = UL_RE.match(line)
        ol = OL_RE.match(line)
        if ul or ol:
            flush_paragraph()
            flush_quote()
            mode = "ul" if ul else "ol"
            item = (ul or ol).group(1)
            if list_mode and list_mode != mode:
                flush_list()
            list_mode = mode
            list_items.append(item)
            continue
        elif list_mode:
            flush_list()

        paragraph.append(line)

    flush_all()
    return "\n".join(out) + ("\n" if out else "")


def _parse_h1(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return fallback


def chapters_from_source(source_file: str, markdown: str, book_number: int | None) -> list[Chapter]:
    if book_number is None:
        title = _parse_h1(markdown, "Prologue")
        body_lines = [line for line in markdown.splitlines() if not line.startswith("# ")]
        return [Chapter("ch-prologue", title, source_file, "\n".join(body_lines).strip())]

    lines = markdown.splitlines()
    book_title = _parse_h1(markdown, f"Book {book_number}")
    sections: list[Chapter] = []
    current_title: str | None = None
    current_number: int | None = None
    current_lines: list[str] = []
    prelude: list[str] = []

    def flush_section() -> None:
        nonlocal current_title, current_number, current_lines
        if current_title is None:
            return
        ordinal = current_number if current_number is not None else len(sections) + 1
        title = strip_numeric_prefix(current_title)
        chapter_id = f"ch-b{book_number:02d}-s{ordinal:02d}-{slugify(title)}"
        sections.append(
            Chapter(
                chapter_id,
                f"{book_title} — {title}",
                source_file,
                "\n".join(current_lines).strip(),
            )
        )
        current_title = None
        current_number = None
        current_lines = []

    for line in lines:
        if line.startswith("# "):
            continue
        match = SECTION_RE.match(line)
        if match:
            flush_section()
            current_number = int(match.group(1)) if match.group(1) else None
            current_title = match.group(2).strip()
            continue
        if current_title is None:
            if line.lstrip().startswith("Status:"):
                continue
            prelude.append(line)
        else:
            current_lines.append(line)

    flush_section()

    if not sections:
        raise ValueError(f"{source_file} contains no ## sections.")

    prelude_text = "\n".join(prelude).strip()
    if prelude_text:
        sections.insert(
            0,
            Chapter(
                f"ch-b{book_number:02d}-intro",
                f"{book_title} — Introduction",
                source_file,
                prelude_text,
            ),
        )

    seen: set[str] = set()
    for chapter in sections:
        if chapter.chapter_id in seen:
            raise ValueError(f"Duplicate generated chapter ID: {chapter.chapter_id}")
        seen.add(chapter.chapter_id)
    return sections


def collect_chapters(source_dir: Path) -> list[Chapter]:
    chapters: list[Chapter] = []
    for filename, book_number in SOURCE_FILES:
        path = source_dir / filename
        if not path.is_file():
            raise FileNotFoundError(f"Required Testament source file missing: {path}")
        chapters.extend(
            chapters_from_source(
                filename,
                path.read_text(encoding="utf-8"),
                book_number,
            )
        )
    return chapters


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def export_to_neo(
    *,
    source_dir: Path,
    output_dir: Path,
    source_commit: str,
    exporter_commit: str,
    author: str = "",
    overwrite: bool = False,
    generated_at: str | None = None,
) -> dict:
    if output_dir.exists():
        if not overwrite:
            raise FileExistsError(
                f"Output directory already exists: {output_dir}. "
                "Pass --overwrite to replace this generated export."
            )
        shutil.rmtree(output_dir)

    chapters = collect_chapters(source_dir)
    output_dir.mkdir(parents=True)
    chapter_dir = output_dir / "chapters"
    chapter_dir.mkdir()

    for chapter in chapters:
        (chapter_dir / f"{chapter.chapter_id}.html").write_text(
            markdown_to_html(chapter.body_markdown),
            encoding="utf-8",
        )

    generated_at = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    book = {
        "id": BOOK_ID,
        "title": BOOK_TITLE,
        "subtitle": "",
        "series": "",
        "author": author,
        "wordGoal": 0,
        "created": generated_at,
        "modified": generated_at,
        "chapterOrder": [chapter.chapter_id for chapter in chapters],
        "chapterTitles": {chapter.chapter_id: chapter.title for chapter in chapters},
        "tabNames": {"notes": "Notes", "outline": "Outline"},
    }
    _write_json(output_dir / "book.json", book)

    (output_dir / "notes.html").write_text("", encoding="utf-8")
    outline = "\n".join(
        f"<p>{html.escape(chapter.title, quote=False)}</p>" for chapter in chapters
    )
    (output_dir / "outline.html").write_text(
        outline + ("\n" if outline else ""),
        encoding="utf-8",
    )
    _write_json(output_dir / "darlings.json", [])
    _write_json(output_dir / "stickies.json", [])

    generated_files = [
        path
        for path in output_dir.rglob("*")
        if path.is_file() and path.name != "TESTAMENT_NEO_EXPORT_RECEIPT.json"
    ]
    hashes = {
        str(path.relative_to(output_dir)).replace("\\", "/"): _sha256(path)
        for path in sorted(generated_files)
    }

    receipt = {
        "schema_version": "testament.neo_export_receipt.v1",
        "source_repository": TESTAMENT_REPOSITORY,
        "source_commit": source_commit,
        "source_files": [
            f"manuscript/draft_v1/{name}" for name, _ in SOURCE_FILES
        ],
        "exporter_version": EXPORTER_VERSION,
        "exporter_commit": exporter_commit,
        "neo_compatibility_commit": NEO_COMPATIBILITY_COMMIT,
        "generated_at": generated_at,
        "generated_files_sha256": hashes,
        "authority": "GENERATED_NON_CANONICAL",
        "reverse_sync": False,
    }
    _write_json(output_dir / "TESTAMENT_NEO_EXPORT_RECEIPT.json", receipt)
    return receipt


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        type=Path,
        required=True,
        help="Path to manuscript/draft_v1",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Caller-supplied export directory",
    )
    parser.add_argument(
        "--source-commit",
        required=True,
        help="Exact Testament source commit",
    )
    parser.add_argument(
        "--exporter-commit",
        required=True,
        help="Exact Testament commit containing this exporter",
    )
    parser.add_argument(
        "--author",
        default="",
        help="Reader-facing author string; blank by default",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing generated output directory",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    export_to_neo(
        source_dir=args.source_dir,
        output_dir=args.output_dir,
        source_commit=args.source_commit,
        exporter_commit=args.exporter_commit,
        author=args.author,
        overwrite=args.overwrite,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
