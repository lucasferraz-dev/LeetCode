# 0485 - Max Consecutive Ones

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

## My Approach

I go through the array once, keeping two variables:

* `cont` counts the size of the current sequence of `1`'s.
* `best` stores the biggest sequence found so far.

For each number:

* If it is `1`, I increase `cont` by `1` and update `best` with `max(best, cont)`.
* If it is `0`, the sequence is broken, so I reset `cont` to `0`.

At the end, `best` holds the size of the longest sequence of `1`'s.

## Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cont = 0
        best = 0
        for i in nums:
            if i == 1:
                cont += 1
                best = max(best, cont)
            else:
                cont = 0
        return best
```

## Complexity

* **Time Complexity:** O(n) - The array is traversed only once.
* **Space Complexity:** O(1) - Only two integer variables are used, regardless of the size of the array.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `3` for `[1, 1, 0, 1, 1, 1]`.
* Example 2: Returns `2` for `[1, 0, 1, 1, 0, 1]`.
* All zeros: Returns `0` when there are no `1`'s.
* All ones: Returns the size of the array when every element is `1`.
* Single element: Returns `1` for `[1]` and `0` for `[0]`.
* Longest at start: Keeps the longest sequence even when it is not the last one.

### Expected Output

```text
test_all_ones ... ok
test_all_zeros ... ok
test_example_one ... ok
test_example_two ... ok
test_longest_at_start ... ok
test_single_element ... ok

----------------------------------------------------------------------
Ran 6 tests

OK
```

Tests can also be executed directly:

```bash
python test_solution.py
```

## LeetCode Result

**Accepted**

* Runtime: **10 ms**
* Runtime percentile: **88.33%**
* Memory: **21.87 MB**
* Memory percentile: **44.32%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to track the current sequence and the best sequence at the same time.
* How to reset a counter when a sequence is broken.
* How to use `max` to keep the best value found so far.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
