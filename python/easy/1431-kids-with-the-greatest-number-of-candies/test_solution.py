import unittest

from solution import Solution


class TestKidsWithCandies(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        candies = [2, 3, 5, 1, 3]
        self.assertEqual(
            self.solution.kidsWithCandies(candies, 3),
            [True, True, True, False, True]
        )

    def test_example_two(self):
        candies = [4, 2, 1, 1, 2]
        self.assertEqual(
            self.solution.kidsWithCandies(candies, 1),
            [True, False, False, False, False]
        )

    def test_example_three(self):
        candies = [12, 1, 12]
        self.assertEqual(
            self.solution.kidsWithCandies(candies, 10),
            [True, False, True]
        )

    def test_single_kid(self):
        candies = [5]
        self.assertEqual(
            self.solution.kidsWithCandies(candies, 0),
            [True]
        )


if __name__ == "__main__":
    unittest.main()
