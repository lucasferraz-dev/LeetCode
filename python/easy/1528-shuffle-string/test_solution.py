import unittest

from solution import Solution


class TestRestoreString(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        s = "codeleet"
        indices = [4, 5, 6, 7, 0, 2, 1, 3]
        self.assertEqual(
            self.solution.restoreString(s, indices),
            "leetcode"
        )

    def test_example_two(self):
        s = "abc"
        indices = [0, 1, 2]
        self.assertEqual(
            self.solution.restoreString(s, indices),
            "abc"
        )

    def test_reversed_indices(self):
        s = "abc"
        indices = [2, 1, 0]
        self.assertEqual(
            self.solution.restoreString(s, indices),
            "cba"
        )

    def test_single_character(self):
        s = "a"
        indices = [0]
        self.assertEqual(
            self.solution.restoreString(s, indices),
            "a"
        )


if __name__ == "__main__":
    unittest.main()
