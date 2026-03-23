import json
import tempfile
import unittest
from pathlib import Path

from typestorm import calculate_result, load_scores, save_scores


class TypeStormTests(unittest.TestCase):
    def test_calculate_result_perfect_match(self):
        wpm, accuracy, time_taken = calculate_result("abcde", "abcde", 0.0, 60.0)
        self.assertEqual(wpm, 1.0)
        self.assertEqual(accuracy, 100.0)
        self.assertEqual(time_taken, 60.0)

    def test_calculate_result_penalizes_extra_characters(self):
        _, accuracy, _ = calculate_result("abc", "abcXYZ", 0.0, 60.0)
        self.assertEqual(accuracy, 50.0)

    def test_calculate_result_penalizes_missing_characters(self):
        _, accuracy, _ = calculate_result("abcdef", "abc", 0.0, 60.0)
        self.assertEqual(accuracy, 50.0)

    def test_load_scores_returns_empty_for_invalid_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "scores.json"
            path.write_text("{bad json}", encoding="utf-8")
            self.assertEqual(load_scores(path), [])

    def test_save_and_load_scores_round_trip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "scores.json"
            scores = [{"round": 1, "level": "Beginner", "wpm": 10.0, "accuracy": 90.0, "time": 12.3}]
            save_scores(scores, path)
            loaded = load_scores(path)
            self.assertEqual(loaded, scores)

    def test_load_scores_returns_empty_for_non_list_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "scores.json"
            path.write_text(json.dumps({"round": 1}), encoding="utf-8")
            self.assertEqual(load_scores(path), [])


if __name__ == "__main__":
    unittest.main()

