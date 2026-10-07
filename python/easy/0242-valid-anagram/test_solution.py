import unittest

from solution import Solution


class TestIsAnagram(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))

    def test_example_two(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))

    def test_different_lengths(self):
        s = "abc"
        t = "abcd"
        self.assertFalse(self.solution.isAnagram(s, t))

    def test_same_letters_different_counts(self):
        s = "aab"
        t = "abb"
        self.assertFalse(self.solution.isAnagram(s, t))

    def test_single_character(self):
        s = "a"
        t = "a"
        self.assertTrue(self.solution.isAnagram(s, t))


if __name__ == "__main__":
    unittest.main()
