import unittest

from solution import Solution


class TestCanConstruct(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        ransomNote = "a"
        magazine = "b"
        self.assertFalse(self.solution.canConstruct(ransomNote, magazine))

    def test_example_two(self):
        ransomNote = "aa"
        magazine = "ab"
        self.assertFalse(self.solution.canConstruct(ransomNote, magazine))

    def test_example_three(self):
        ransomNote = "aa"
        magazine = "aab"
        self.assertTrue(self.solution.canConstruct(ransomNote, magazine))

    def test_same_strings(self):
        ransomNote = "abc"
        magazine = "abc"
        self.assertTrue(self.solution.canConstruct(ransomNote, magazine))

    def test_different_order(self):
        ransomNote = "abc"
        magazine = "cbadef"
        self.assertTrue(self.solution.canConstruct(ransomNote, magazine))

    def test_ransom_note_longer(self):
        ransomNote = "aab"
        magazine = "ab"
        self.assertFalse(self.solution.canConstruct(ransomNote, magazine))


if __name__ == "__main__":
    unittest.main()
