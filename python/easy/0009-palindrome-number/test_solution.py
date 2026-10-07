import unittest

from solution import Solution


class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        x = 121
        self.assertTrue(self.solution.isPalindrome(x))

    def test_example_two(self):
        x = -121
        self.assertFalse(self.solution.isPalindrome(x))

    def test_example_three(self):
        x = 10
        self.assertFalse(self.solution.isPalindrome(x))

    def test_zero(self):
        x = 0
        self.assertTrue(self.solution.isPalindrome(x))

    def test_single_digit(self):
        x = 7
        self.assertTrue(self.solution.isPalindrome(x))

    def test_even_length_palindrome(self):
        x = 1221
        self.assertTrue(self.solution.isPalindrome(x))


if __name__ == "__main__":
    unittest.main()
