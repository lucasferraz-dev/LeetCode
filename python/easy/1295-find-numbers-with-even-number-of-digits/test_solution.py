import unittest

from solution import Solution


class TestFindNumbers(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [12, 345, 2, 6, 7896]
        self.assertEqual(self.solution.findNumbers(nums), 2)

    def test_example_two(self):
        nums = [555, 901, 482, 1771]
        self.assertEqual(self.solution.findNumbers(nums), 1)

    def test_single_digits(self):
        nums = [1, 2, 3, 9]
        self.assertEqual(self.solution.findNumbers(nums), 0)

    def test_all_even(self):
        nums = [10, 99, 1000, 123456]
        self.assertEqual(self.solution.findNumbers(nums), 4)

    def test_upper_bound(self):
        nums = [100000]
        self.assertEqual(self.solution.findNumbers(nums), 1)


if __name__ == "__main__":
    unittest.main()
