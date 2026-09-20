import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "plan_neo_install.py"
SPEC = importlib.util.spec_from_file_location("plan_neo_install", MODULE_PATH)
planner = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = planner
SPEC.loader.exec_module(planner)


class NeoInstallPlannerTests(unittest.TestCase):
    def _write_json(self, path: Path, value) -> None:
        path.write_text(json.dumps(value), encoding="utf-8")

    def _make_staged_book(self, root: Path, book_id: str = "book-testament-of-the-spark") -> Path:
        staged = root / "staged"
        chapters = staged / "chapters"
        chapters.mkdir(parents=True)
        chapter_ids = ["ch-prologue", "ch-b01-s01-first"]
        self._write_json(
            staged / "book.json",
            {
                "id": book_id,
                "title": "The Testament of the Spark",
                "chapterOrder": chapter_ids,
                "tabNames": {"notes": "Notes", "outline": "Outline"},
            },
        )
        for chapter_id in chapter_ids:
            (chapters / f"{chapter_id}.html").write_text("<p>Text.</p>", encoding="utf-8")
        (staged / "notes.html").write_text("", encoding="utf-8")
        (staged / "outline.html").write_text("", encoding="utf-8")
        self._write_json(staged / "darlings.json", [])
        self._write_json(staged / "stickies.json", [])
        self._write_json(
            staged / "TESTAMENT_NEO_EXPORT_RECEIPT.json",
            {
                "source_repository": "thebrazenbeard/testament",
                "source_commit": "a" * 40,
                "exporter_commit": "b" * 40,
                "neo_compatibility_commit": "c" * 40,
            },
        )
        return staged

    def test_builds_non_mutating_plan_for_single_shelf(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            staged = self._make_staged_book(root)
            library_json = root / "NEO Library" / "library.json"
            library_json.parent.mkdir()
            self._write_json(
                library_json,
                {
                    "shelves": [
                        {
                            "id": "shelf-1",
                            "name": "Works in Progress",
                            "bookIds": [],
                        }
                    ]
                },
            )

            plan = planner.build_install_plan(
                staged_dir=staged,
                library_json=library_json,
            )

            self.assertFalse(plan["apply"])
            self.assertEqual(
                plan["book"]["required_target_directory_name"],
                "book-testament-of-the-spark",
            )
            self.assertEqual(plan["library"]["shelf_id"], "shelf-1")
            self.assertEqual(
                plan["library"]["mutation"]["value"],
                "book-testament-of-the-spark",
            )
            self.assertIn("NO_LIBRARY_JSON_MODIFIED", plan["guards"])
            self.assertTrue(plan["warnings"])
            self.assertIn("Anonymous", plan["warnings"][0])
            self.assertFalse((library_json.parent / "book-testament-of-the-spark").exists())

    def test_multiple_shelves_require_explicit_shelf(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            staged = self._make_staged_book(root)
            library_json = root / "library.json"
            self._write_json(
                library_json,
                {
                    "shelves": [
                        {"id": "one", "name": "One", "bookIds": []},
                        {"id": "two", "name": "Two", "bookIds": []},
                    ]
                },
            )

            with self.assertRaises(ValueError):
                planner.build_install_plan(
                    staged_dir=staged,
                    library_json=library_json,
                )

            plan = planner.build_install_plan(
                staged_dir=staged,
                library_json=library_json,
                shelf_id="two",
            )
            self.assertEqual(plan["library"]["shelf_id"], "two")

    def test_refuses_existing_registration_or_target_directory(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            staged = self._make_staged_book(root)
            library_dir = root / "NEO Library"
            library_dir.mkdir()
            library_json = library_dir / "library.json"
            self._write_json(
                library_json,
                {
                    "shelves": [
                        {
                            "id": "shelf-1",
                            "name": "Works in Progress",
                            "bookIds": ["book-testament-of-the-spark"],
                        }
                    ]
                },
            )
            with self.assertRaises(ValueError):
                planner.build_install_plan(
                    staged_dir=staged,
                    library_json=library_json,
                )

            self._write_json(
                library_json,
                {
                    "shelves": [
                        {
                            "id": "shelf-1",
                            "name": "Works in Progress",
                            "bookIds": [],
                        }
                    ]
                },
            )
            (library_dir / "book-testament-of-the-spark").mkdir()
            with self.assertRaises(FileExistsError):
                planner.build_install_plan(
                    staged_dir=staged,
                    library_json=library_json,
                )


if __name__ == "__main__":
    unittest.main()
