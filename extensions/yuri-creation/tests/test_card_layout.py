"""Focused synthetic regressions for V3 mirrors and fenced HTML text edits."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
spec = importlib.util.spec_from_file_location("layout_cards", ROOT / "shared/card_files.py")
cards = importlib.util.module_from_spec(spec); spec.loader.exec_module(cards)
p = cards.p


def menu(label="Choose"):
    return ("```htm\n<div class=\"menu\" onclick=\"keep()\">"
            f"<b>{label}</b>{{{{user}}}}<script>const keep=1;</script>"
            "<style>.menu{color:red}</style></div>\n```")


def fixture():
    first = menu()
    return {
        "spec": "chara_card_v3", "spec_version": "3.0", "name": "Synthetic",
        "first_mes": first, "description": "same", "tags": ["one"],
        "data": {
            "name": "Synthetic", "first_mes": first, "description": "same", "tags": ["one"],
            "alternate_greetings": ["top-only"],
            "extensions": {"regex_scripts": [{"findRegex": "SAFE", "replaceString": first, "disabled": False}],
                           "private_setting": {"keep": 7}},
            "character_book": {"name": "unmodified", "entries": [{"content": "keep"}]},
        },
        "alternate_greetings": ["data-only"],
        "extensions": {"regex_scripts": [{"findRegex": "SAFE", "replaceString": first, "disabled": False}],
                       "private_setting": {"keep": 7}},
    }


class CardLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source.json"
        self.source.write_text(json.dumps(fixture(), ensure_ascii=False), encoding="utf-8")
        self.project = self.root / "project"
        self.opened = cards.open_project(self.source, self.project)

    def make_plan(self, changes):
        path = self.project / "edit-plan.json"
        plan = p.read(path)
        plan["agent_review"] = {"completed": True, "notes": ["Reviewed synthetic mirror and display-text scope."]}
        plan["decisions"] = [{"kind": "preserved", "summary": "Preserve synthetic card facts."}]
        plan["changes"] = changes
        path.write_text(json.dumps(plan, ensure_ascii=False), encoding="utf-8")
        return path

    def change(self, path, before, after, mode="prose"):
        item = {"document": "json", "path": path, "before": before, "after": after,
                "reason": "Adapt synthetic display prose"}
        if mode:
            item["edit_mode"] = mode
        return item

    def apply_changes(self, changes, name="result"):
        return cards.apply(self.project, self.make_plan(changes), self.root / name)

    def test_open_reports_layout_and_divergent_existing_mirrors(self):
        info = self.opened["documents"]["json"]
        self.assertIn("first_mes", info["mirrors"])
        self.assertIn("tags", info["mirrors"])
        self.assertIn("alternate_greetings", info["divergent_mirrors"])
        self.assertTrue(info["renderer_copies"])

    def test_one_sided_equal_and_divergent_mirror_edits_name_missing_pointer(self):
        source = p.read(self.project / "documents.json")["json"]
        old = source["first_mes"]
        with self.assertRaisesRegex(ValueError, r"/data/first_mes"):
            self.apply_changes([self.change("/first_mes", old, menu("Updated"), "html_text")])
        self.assertFalse((self.root / "result").exists())
        with self.assertRaisesRegex(ValueError, r"/data/alternate_greetings"):
            self.apply_changes([self.change("/alternate_greetings/0", "data-only", "updated")], "divergent")
        self.assertFalse((self.root / "divergent").exists())

    def test_tags_mirror_requires_both_explicit_paths(self):
        old = ["one"]
        with self.assertRaisesRegex(ValueError, r"/data/tags"):
            self.apply_changes([self.change("/tags", old, ["two"])])
        self.assertFalse((self.root / "result").exists())
        self.apply_changes([self.change("/tags", old, ["two"]),
                            self.change("/data/tags", old, ["two"])], "tags-result")
        result = p.read(self.root / "tags-result" / "character.json")
        self.assertEqual(result["tags"], result["data"]["tags"])

    def test_coordinated_mirrors_nested_greetings_and_renderer_copies_apply(self):
        source = p.read(self.project / "documents.json")["json"]
        old = source["first_mes"]; new = menu("Updated")
        changes = [
            self.change("/first_mes", old, new, "html_text"),
            self.change("/data/first_mes", old, new, "html_text"),
            self.change("/extensions/regex_scripts/0/replaceString", old, new, "html_text"),
            self.change("/data/extensions/regex_scripts/0/replaceString", old, new, "html_text"),
            self.change("/alternate_greetings/0", "data-only", "greeting"),
            self.change("/data/alternate_greetings/0", "top-only", "greeting"),
        ]
        self.apply_changes(changes)
        result = p.read(self.root / "result" / "character.json")
        self.assertEqual(result["first_mes"], result["data"]["first_mes"])
        self.assertEqual(result["data"]["first_mes"], result["data"]["extensions"]["regex_scripts"][0]["replaceString"])
        self.assertEqual(result["alternate_greetings"], result["data"]["alternate_greetings"])
        self.assertEqual(result["extensions"]["private_setting"], {"keep": 7})
        self.assertEqual(result["data"]["character_book"]["entries"][0]["content"], "keep")

    def test_html_text_rejects_structure_code_macros_and_unknown_modes(self):
        old = menu()
        bad_values = [
            old.replace('class="menu"', 'class="changed"'),
            old.replace('onclick="keep()"', 'onclick="run()"'),
            old.replace("const keep=1", "const keep=2"),
            old.replace("color:red", "color:blue"),
            old.replace("{{user}}", "{{char}}"),
            old.replace("<b>Choose</b>{{user}}", "{{user}}<b>Choose</b>"),
            old.replace("<script>const keep=1;</script>", "<script/>"),
            old.replace("```htm", "```python"),
        ]
        for bad in bad_values:
            with self.subTest(value=bad), self.assertRaises(ValueError):
                cards.protect_code(old, bad, "json:/first_mes", "html_text")
        with self.assertRaisesRegex(ValueError, "fenced code"):
            cards.protect_code(old, menu("Changed"), "json:/first_mes")
        tilde_fence = "~~~python\nprint('keep')\n~~~"
        with self.assertRaisesRegex(ValueError, "fenced code"):
            cards.protect_code(tilde_fence, "~~~python\nprint('change')\n~~~", "json:/description")
        non_html_fence = "```python\nprint('keep')\n```"
        with self.assertRaises(ValueError):
            cards.protect_code(non_html_fence, "```python\nprint('change')\n```", "json:/description", "html_text")
        with self.assertRaisesRegex(ValueError, "Protected field"):
            change = self.change("/data/extensions/regex_scripts/0/findRegex", "SAFE", "CHANGED", "html_text")
            self.apply_changes([change], "regex-logic")
        with self.assertRaisesRegex(ValueError, "Unsupported edit_mode"):
            change = self.change("/first_mes", old, menu("Updated"), "future-mode")
            self.apply_changes([change], "unknown-mode")


if __name__ == "__main__":
    unittest.main()
