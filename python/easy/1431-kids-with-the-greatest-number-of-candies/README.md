# 1431 - Kids With the Greatest Number of Candies

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i-th` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i-th` kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `false` otherwise.

Note that multiple kids can have the greatest number of candies.

## My Approach

To know whether a kid can have the greatest number of candies, I only need to compare their total with the current maximum.

My first solution sorted the list with `sorted()` using `reverse=True` and took the first element as the greatest number to compare against.

However, sorting takes O(n log n), which is more work than needed just to find the largest value. So I decided to use `max()` instead, which finds the maximum in O(n).

After calculating the maximum once, I iterate through the array and, for each kid, check whether their candies plus `extraCandies` are greater than or equal to the maximum, appending the boolean result to the list.

## Solution

```python
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        maj = max(candies)
        for i in candies:
            res.append(i + extraCandies >= maj)
        return res
```

## Complexity

* **Time Complexity:** O(n) - Finding the maximum takes O(n) and the loop through the array takes another O(n).
* **Space Complexity:** O(n) - The result list stores one boolean for each kid.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Most kids can reach the maximum with the extra candies.
* Example 2: Only the kid who already has the maximum stays on top.
* Example 3: Handles multiple kids sharing the greatest number of candies.
* Single kid: Validates the result when only one kid is present.

### Expected Output

```text
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_single_kid ... ok

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
* Runtime percentile: **100%**
* Memory: **19.27 MB**
* Memory percentile: **64.66%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* Why sorting is unnecessary when only the maximum value is needed.
* How to use `max()` to find the greatest value in O(n) instead of sorting in O(n log n).
* How to calculate a value once before the loop instead of recalculating it on every iteration.
* How a comparison expression returns a boolean that can be stored directly.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
