
import unittest

from solution import Solution

class TestMaximumWealth(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        accounts = [[1, 2, 3], [3, 2, 1]]
        self.assertEqual(self.solution.maximumWealth(accounts), 6)

    def test_example_two(self):
        accounts = [[1, 5], [7, 3], [3, 5]]
        self.assertEqual(self.solution.maximumWealth(accounts), 10)

    def test_example_three(self):
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        self.assertEqual(self.solution.maximumWealth(accounts), 17)

    def test_single_customer(self):
        accounts = [[4, 5, 6]]
        self.assertEqual(self.solution.maximumWealth(accounts), 15)


if __name__ == "__main__":
    unittest.main()