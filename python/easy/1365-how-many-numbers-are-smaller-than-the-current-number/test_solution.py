import unittest

from solution import Solution


class TestSmallerNumbersThanCurrent(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [8, 1, 2, 2, 3]
        self.assertEqual(
            self.solution.smallerNumbersThanCurrent(nums),
            [4, 0, 1, 1, 3]
        )

    def test_example_two(self):
        nums = [6, 5, 4, 8]
        self.assertEqual(
            self.solution.smallerNumbersThanCurrent(nums),
            [2, 1, 0, 3]
        )

    def test_example_three(self):
        nums = [7, 7, 7, 7]
        self.assertEqual(
            self.solution.smallerNumbersThanCurrent(nums),
            [0, 0, 0, 0]
        )

    def test_single_element(self):
        nums = [5]
        self.assertEqual(
            self.solution.smallerNumbersThanCurrent(nums),
            [0]
        )


if __name__ == "__main__":
    unittest.main()
