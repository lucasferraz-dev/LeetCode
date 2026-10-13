import unittest

from solution import Solution


class TestSortedSquares(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [-4, -1, 0, 3, 10]
        self.assertEqual(self.solution.sortedSquares(nums), [0, 1, 9, 16, 100])

    def test_example_two(self):
        nums = [-7, -3, 2, 3, 11]
        self.assertEqual(self.solution.sortedSquares(nums), [4, 9, 9, 49, 121])

    def test_all_negative(self):
        nums = [-5, -3, -2, -1]
        self.assertEqual(self.solution.sortedSquares(nums), [1, 4, 9, 25])

    def test_all_positive(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.solution.sortedSquares(nums), [1, 4, 9, 16])

    def test_single_element(self):
        nums = [-3]
        self.assertEqual(self.solution.sortedSquares(nums), [9])


if __name__ == "__main__":
    unittest.main()
