import unittest

from solution import Solution


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [5, 4, 2, 3]
        self.assertEqual(self.solution.numberGame(nums), [3, 2, 5, 4])

    def test_example_two(self):
        nums = [2, 5]
        self.assertEqual(self.solution.numberGame(nums), [5, 2])

    def test_already_sorted(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.numberGame(nums), [2, 1, 4, 3, 6, 5])

    def test_reverse_sorted(self):
        nums = [6, 5, 4, 3, 2, 1]
        self.assertEqual(self.solution.numberGame(nums), [2, 1, 4, 3, 6, 5])

    def test_duplicates(self):
        nums = [3, 1, 3, 1]
        self.assertEqual(self.solution.numberGame(nums), [1, 1, 3, 3])


if __name__ == "__main__":
    unittest.main()
