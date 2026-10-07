import unittest

from solution import Solution


class TestNumIdenticalPairs(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [1, 2, 3, 1, 1, 3]
        self.assertEqual(
            self.solution.numIdenticalPairs(nums),
            4
        )

    def test_example_two(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(
            self.solution.numIdenticalPairs(nums),
            6
        )

    def test_example_three(self):
        nums = [1, 2, 3]
        self.assertEqual(
            self.solution.numIdenticalPairs(nums),
            0
        )

    def test_single_element(self):
        nums = [1]
        self.assertEqual(
            self.solution.numIdenticalPairs(nums),
            0
        )


if __name__ == "__main__":
    unittest.main()
