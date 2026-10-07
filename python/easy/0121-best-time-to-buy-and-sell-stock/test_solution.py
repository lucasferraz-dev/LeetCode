import unittest

from solution import Solution


class TestMaxProfit(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(
            self.solution.maxProfit(prices),
            5
        )

    def test_example_two(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(
            self.solution.maxProfit(prices),
            0
        )

    def test_single_price(self):
        prices = [5]
        self.assertEqual(
            self.solution.maxProfit(prices),
            0
        )

    def test_lowest_price_after_best_profit(self):
        prices = [3, 8, 1, 4]
        self.assertEqual(
            self.solution.maxProfit(prices),
            5
        )

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(
            self.solution.maxProfit(prices),
            4
        )


if __name__ == "__main__":
    unittest.main()
