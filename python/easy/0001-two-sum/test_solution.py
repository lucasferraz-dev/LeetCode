
import unittest

from solution import Solution


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [2, 7, 11, 15]
        target = 9

        self.assertEqual(
            self.solution.twoSum(nums, target),
            [0, 1]
        )

    def test_example_two(self):
        nums = [3, 2, 4]
        target = 6

        self.assertEqual(
            self.solution.twoSum(nums, target),
            [1, 2]
        )

    def test_example_three(self):
        nums = [3, 3]
        target = 6

        self.assertEqual(
            self.solution.twoSum(nums, target),
            [0, 1]
        )


if __name__ == "__main__":
    unittest.main()