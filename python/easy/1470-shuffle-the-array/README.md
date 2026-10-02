# 1470 - Shuffle the Array

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given the array `nums` consisting of `2n` elements in the form `[x1, x2, ..., xn, y1, y2, ..., yn]`.

Return the array in the form `[x1, y1, x2, y2, ..., xn, yn]`.

## My Approach

The array can be seen as two halves: the first `n` elements are the `x` values and the last `n` elements are the `y` values.

For each index `i` from `0` to `n - 1`, the element `nums[i]` belongs to the first half and its pair `nums[i + n]` is in the same position of the second half.

So I iterate through the first half and, at each step, append `nums[i]` followed by `nums[i + n]` to the result list, which builds the interleaved array in order.

## Solution

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
```

## Complexity

* **Time Complexity:** O(n) - The loop runs `n` times and each iteration performs two constant-time appends.
* **Space Complexity:** O(n) - The result list stores all `2n` elements.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Interleaves an array with three pairs.
* Example 2: Interleaves an array with four pairs and repeated values.
* Example 3: Handles an array where each half contains identical values.
* Single pair: Validates the result when `n = 1`.

### Expected Output

```text
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_single_pair ... ok

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

* Runtime: **66 ms**
* Runtime percentile: **41.22%**
* Memory: **19.33 MB**
* Memory percentile: **56.72%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to split an array into two logical halves using index offsets.
* How the index `i + n` maps an element of the first half to its pair in the second half.
* How to build a new list by interleaving elements from two sequences.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
