import unittest

from solution import Solution


class TestRunningSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(
            self.solution.runningSum(nums),
            [1, 3, 6, 10]
        )

    def test_example_two(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(
            self.solution.runningSum(nums),
            [1, 2, 3, 4, 5]
        )

    def test_example_three(self):
        nums = [3, 1, 2, 10, 1]
        self.assertEqual(
            self.solution.runningSum(nums),
            [3, 4, 6, 16, 17]
        )

    def test_single_element(self):
        nums = [5]
        self.assertEqual(
            self.solution.runningSum(nums),
            [5]
        )


if __name__ == "__main__":
    unittest.main()
