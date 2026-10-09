import unittest

from solution import Solution


class TestFindMaxConsecutiveOnes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [1, 1, 0, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_example_two(self):
        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 2)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_all_ones(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 4)

    def test_single_element(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1]), 1)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0]), 0)

    def test_longest_at_start(self):
        nums = [1, 1, 1, 0, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)


if __name__ == "__main__":
    unittest.main()
