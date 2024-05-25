import unittest

from lab_7_2 import find_max_substring_multiplicity


class TestFindMaxSubstringMultiplicity(unittest.TestCase):
    def test_substring_appears_multiple_times(self):
        word = "abcabcabc"
        substring = "abc"
        result = find_max_substring_multiplicity(word, substring)
        self.assertEqual(result, 3)

    def test_substring_is_longer_than_word(self):
        word = "abc"
        substring = "abcdef"
        result = find_max_substring_multiplicity(word, substring)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
