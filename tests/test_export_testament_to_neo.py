import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "export_testament_to_neo.py"
SPEC = importlib.util.spec_from_file_location("export_testament_to_neo", MODULE_PATH)
neo = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = neo
SPEC.loader.exec_module(neo)


class ExporterTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(
            neo.slugify("Under Other Men's Flags"),
            "under-other-mens-flags",
        )
        self.assertEqual(
            neo.slugify("Yeshua — The Man"),
            "yeshua-the-man",
        )

    def test_sections_generate_stable_ids(self):
        source = """# Book I — The World

## 1. Under Other Men's Flags

First.

## 2. The God of Israel

Second.
"""
        chapters = neo.chapters_from_source(
            "BOOK_I_THE_WORLD.md",
            source,
            1,
        )
        self.assertEqual(
            [chapter.chapter_id for chapter in chapters],
            [
                "ch-b01-s01-under-other-mens-flags",
                "ch-b01-s02-the-god-of-israel",
            ],
        )

    def test_markdown_subset_renders_without_raw_heading_markers(self):
        source = """### Small heading

A **strong** and *soft* line with [link](https://example.com/a_b).

> quoted
> text

- one
- two

***
"""
        rendered = neo.markdown_to_html(source)
        self.assertIn("<h4>Small heading</h4>", rendered)
        self.assertIn("<strong>strong</strong>", rendered)
        self.assertIn("<em>soft</em>", rendered)
        self.assertIn(
            '<a href="https://example.com/a_b">link</a>',
            rendered,
        )
        self.assertIn(
            "<blockquote><p>quoted text</p></blockquote>",
            rendered,
        )
        self.assertIn(
            "<ul><li>one</li><li>two</li></ul>",
            rendered,
        )
        self.assertIn(
            '<p class="scene-break">***</p>',
            rendered,
        )
        self.assertNotIn("### ", rendered)

    def _write_fixture_sources(self, root: Path) -> None:
        for filename, book_number in neo.SOURCE_FILES:
            if book_number is None:
                content = (
                    "# Prologue — This Is Not a Lost Gospel\n\n"
                    "Opening prose.\n"
                )
            else:
                content = (
                    f"# Book {book_number} — Fixture\n\n"
                    f"## 1. Section One\n\n"
                    f"Book {book_number} prose.\n"
                )
            (root / filename).write_text(
                content,
                encoding="utf-8",
            )

    def test_export_contract_and_overwrite_guard(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            source = base / "source"
            output = base / "neo"
            source.mkdir()
            self._write_fixture_sources(source)

            receipt = neo.export_to_neo(
                source_dir=source,
                output_dir=output,
                source_commit="a" * 40,
                exporter_commit="b" * 40,
                generated_at="2026-09-20T00:00:00Z",
            )

            book = json.loads(
                (output / "book.json").read_text(encoding="utf-8")
            )
            self.assertEqual(len(book["chapterOrder"]), 9)
            self.assertEqual(
                book["chapterOrder"][0],
                "ch-prologue",
            )
            self.assertEqual(
                receipt["authority"],
                "GENERATED_NON_CANONICAL",
            )
            self.assertFalse(receipt["reverse_sync"])
            self.assertEqual(
                receipt["source_commit"],
                "a" * 40,
            )
            self.assertEqual(
                receipt["exporter_commit"],
                "b" * 40,
            )
            self.assertEqual(
                set(book["chapterOrder"]),
                {
                    path.stem
                    for path in (output / "chapters").glob("*.html")
                },
            )

            with self.assertRaises(FileExistsError):
                neo.export_to_neo(
                    source_dir=source,
                    output_dir=output,
                    source_commit="a" * 40,
                    exporter_commit="b" * 40,
                )

            neo.export_to_neo(
                source_dir=source,
                output_dir=output,
                source_commit="a" * 40,
                exporter_commit="b" * 40,
                overwrite=True,
                generated_at="2026-09-20T00:00:00Z",
            )

    def test_control_status_prelude_is_not_rendered(self):
        source = """# Book VII — The Kingdom Within

Status: EXPLICIT MODERN INTERPRETATION

## 1. The Problem of the Sky

Text.
"""
        chapters = neo.chapters_from_source(
            "BOOK_VII_THE_KINGDOM_WITHIN.md",
            source,
            7,
        )
        self.assertEqual(len(chapters), 1)
        self.assertNotIn(
            "Status:",
            chapters[0].body_markdown,
        )

    def test_preserves_reader_prelude_as_intro_chapter(self):
        source = """# Book VII — The Kingdom Within

Status: EXPLICIT MODERN INTERPRETATION

Nothing in this book is presented as recovered ancient teaching.

## 1. The Problem of the Sky

Text.
"""
        chapters = neo.chapters_from_source(
            "BOOK_VII_THE_KINGDOM_WITHIN.md",
            source,
            7,
        )
        self.assertEqual(
            [chapter.chapter_id for chapter in chapters],
            [
                "ch-b07-intro",
                "ch-b07-s01-the-problem-of-the-sky",
            ],
        )
        self.assertEqual(
            chapters[0].title,
            "Book VII — The Kingdom Within — Introduction",
        )
        self.assertEqual(
            chapters[0].body_markdown,
            "Nothing in this book is presented as recovered ancient teaching.",
        )
        self.assertNotIn("Status:", chapters[0].body_markdown)


if __name__ == "__main__":
    unittest.main()
