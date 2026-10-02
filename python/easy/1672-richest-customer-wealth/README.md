# 1672 - Richest Customer Wealth

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` represents the amount of money the `i-th` customer has in the `j-th` bank.

Return the wealth that the richest customer has.

A customer's wealth is the total amount of money they have in all their bank accounts.

## My Approach

My initial approach was to use nested loops to calculate the total wealth of each customer.

During development, I encountered some mistakes, such as:

* Using the index instead of the actual value inside the loop.
* Forgetting to reset the accumulator for each customer.
* Confusing the customer's total wealth with the individual account values.
* Updating the maximum wealth incorrectly.

After understanding the problem better, I simplified the solution using Python's built-in `sum()` and `max()` functions.

The `sum()` function calculates the total wealth of each customer, while `max()` returns the highest total.

## Solution

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)
```

## Complexity

* **Time Complexity:** O(m × n) - Each account value is visited once to calculate the customers' wealth.
* **Space Complexity:** O(1) auxiliary space - The solution does not create an additional list to store the wealth totals.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Two customers with equal wealth.
* Example 2: Three customers with different wealth totals.
* Example 3: Three customers with different account balances.
* Single customer: Validates the result when only one customer is present.

### Expected Output

```text
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_single_customer ... ok

----------------------------------------------------------------------
Ran 4 tests

OK
```

Tests can also be executed directly:

```bash
python test_solution.py
```

## LeetCode Result

**Accepted**

* Runtime: **0 ms**
* Runtime percentile: **100.00%**
* Memory: **19.34 MB**
* Memory percentile: **44.55%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to calculate totals using nested lists.
* How to use `sum()` and `max()` to simplify Python solutions.
* How generator expressions can avoid creating an additional list.
* How to identify and correct logical errors involving accumulators and indexes.
* How to analyze time and auxiliary space complexity.
* How to validate a solution using automated unit tests.
