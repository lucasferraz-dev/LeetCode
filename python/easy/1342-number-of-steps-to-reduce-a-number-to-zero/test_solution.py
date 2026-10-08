import unittest

from solution import Solution


class TestNumberOfSteps(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        num = 14
        self.assertEqual(self.solution.numberOfSteps(num), 6)

    def test_example_two(self):
        num = 8
        self.assertEqual(self.solution.numberOfSteps(num), 4)

    def test_example_three(self):
        num = 123
        self.assertEqual(self.solution.numberOfSteps(num), 12)

    def test_zero(self):
        num = 0
        self.assertEqual(self.solution.numberOfSteps(num), 0)

    def test_one(self):
        num = 1
        self.assertEqual(self.solution.numberOfSteps(num), 1)

    def test_power_of_two(self):
        num = 1024
        self.assertEqual(self.solution.numberOfSteps(num), 11)


if __name__ == "__main__":
    unittest.main()
