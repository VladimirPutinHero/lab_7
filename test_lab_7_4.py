import unittest
from lab_7_4 import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):
    def test_same_strings(self):
        string1 = "hello"
        string2 = "hello"
        result = levenshtein_distance(string1, string2)
        self.assertEqual(result, 0)

    def test_one_empty_string(self):
        string1 = "hello"
        string2 = ""
        result = levenshtein_distance(string1, string2)
        self.assertEqual(result, 5)

    def test_different_strings(self):
        string1 = "kitten"
        string2 = "sitting"
        result = levenshtein_distance(string1, string2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
