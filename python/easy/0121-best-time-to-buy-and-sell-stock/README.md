# 0121 - Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## My Approach

To get the best profit when selling on a given day, I need to have bought at the lowest price seen before that day.

So instead of comparing every pair of days, I go through the prices only once and keep track of two values:

* `lowest`: the lowest price seen so far, which is the best day to buy.
* `bestProfit`: the highest profit found so far.

For each price, I calculate the profit of selling on that day (`i - lowest`) and update `bestProfit` if it is higher. Then, if the current price is lower than `lowest`, it becomes the new best price to buy for the following days.

Since `bestProfit` starts at `0`, if the prices only go down, no positive profit is ever found and the answer is `0`.

## Solution

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        bestProfit = 0
        profit = 0
        for i in prices:
            profit = i - lowest
            if profit > bestProfit:
                bestProfit = profit
            if i < lowest:
                lowest = i

        return bestProfit
```

## Complexity

* **Time Complexity:** O(n) - The array is traversed only once.
* **Space Complexity:** O(1) - Only a few variables are used, regardless of the size of `prices`.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Finds the maximum profit when buying low and selling later.
* Example 2: Returns `0` when the prices only go down.
* Single price: Returns `0` when there is only one day.
* Lowest price after best profit: Keeps the best profit even when a lower price appears later.
* Increasing prices: Buys on the first day and sells on the last one.

### Expected Output

```text
test_example_one ... ok
test_example_two ... ok
test_increasing_prices ... ok
test_lowest_price_after_best_profit ... ok
test_single_price ... ok

----------------------------------------------------------------------
Ran 5 tests

OK
```

Tests can also be executed directly:

```bash
python test_solution.py
```

## LeetCode Result

**Accepted**

* Runtime: **19 ms**
* Runtime percentile: **95.75%**
* Memory: **28.58 MB**
* Memory percentile: **77.20%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to keep track of the minimum value seen so far while iterating.
* How to avoid an O(n²) brute-force solution by solving the problem in a single pass.
* Why the buy day must always come before the sell day, and how the order of the checks guarantees that.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
