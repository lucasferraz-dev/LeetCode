# 1512 - Number of Good Pairs

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given an array of integers `nums`, return the number of good pairs.

A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

## My Approach

Instead of comparing every pair of elements, I used a dictionary to count how many times each number has already appeared.

When I find a number that was already seen, it forms a good pair with each previous occurrence. So I add `seen[i]` to the counter and then increment the number of occurrences of that value.

If the number has not appeared yet, I simply register it in the dictionary with a count of `1`.

This way, all good pairs are counted in a single pass through the array.

## Solution

```python
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        seen = {}
        cont = 0
        for i in nums:
            if i in seen:
                cont += seen[i]
                seen[i] += 1
            else:
                seen[i] = 1
        return cont
```

## Complexity

* **Time Complexity:** O(n) - Each element is visited once, and dictionary lookups and updates take O(1) on average.
* **Space Complexity:** O(n) - In the worst case, the dictionary stores every distinct value in `nums`.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Counts good pairs in an array with repeated values.
* Example 2: Handles an array where all elements are equal.
* Example 3: Returns `0` when there are no repeated values.
* Single element: Returns `0` when the array has only one element.

### Expected Output

```text
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_single_element ... ok

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
* Memory: **19.25 MB**
* Memory percentile: **55.41%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to use a dictionary to count occurrences while iterating.
* How each new occurrence of a value forms a pair with all previous occurrences.
* How to avoid an O(n²) brute-force solution by counting in a single pass.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
