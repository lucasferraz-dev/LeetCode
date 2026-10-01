import unittest

from solution import Solution


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(
            self.solution.fizzBuzz(3),
            ["1", "2", "Fizz"]
        )

    def test_example_two(self):
        self.assertEqual(
            self.solution.fizzBuzz(5),
            ["1", "2", "Fizz", "4", "Buzz"]
        )

    def test_example_three(self):
        self.assertEqual(
            self.solution.fizzBuzz(15),
            [
                "1", "2", "Fizz", "4", "Buzz",
                "Fizz", "7", "8", "Fizz", "Buzz",
                "11", "Fizz", "13", "14", "FizzBuzz"
            ]
        )

    def test_fizzbuzz_multiple(self):
        self.assertEqual(
            self.solution.fizzBuzz(30)[-1],
            "FizzBuzz"
        )


if __name__ == "__main__":
    unittest.main()