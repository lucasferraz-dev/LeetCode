import unittest

from solution import Solution


class TestShuffle(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [2, 5, 1, 3, 4, 7]
        self.assertEqual(
            self.solution.shuffle(nums, 3),
            [2, 3, 5, 4, 1, 7]
        )

    def test_example_two(self):
        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        self.assertEqual(
            self.solution.shuffle(nums, 4),
            [1, 4, 2, 3, 3, 2, 4, 1]
        )

    def test_example_three(self):
        nums = [1, 1, 2, 2]
        self.assertEqual(
            self.solution.shuffle(nums, 2),
            [1, 2, 1, 2]
        )

    def test_single_pair(self):
        nums = [1, 2]
        self.assertEqual(
            self.solution.shuffle(nums, 1),
            [1, 2]
        )


if __name__ == "__main__":
    unittest.main()
