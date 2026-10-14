# 1089 - Duplicate Zeros

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

**Note** that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

## My Approach: Insert and Pop

I walk through the array with an index `i` and keep the length fixed by removing one element every time I add one:

* If `arr[i]` is zero, I insert another `0` at position `i`, which shifts everything to the right.
* Then I `pop()` the last element so the array keeps its original length.
* I jump `i` forward by 2 to skip both zeros, so the new zero is not duplicated again.
* Otherwise I just move `i` forward by 1.

The loop stops at `j = len(arr) - 1`. A zero in the last position does not need to be duplicated, because its copy would fall outside the array anyway.

## Solution

```python
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        j = len(arr) - 1
        i = 0
        while i < j:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2
                arr.pop()
            else:
                i += 1
```

## Complexity

* **Time Complexity:** O(n^2) - Each `insert` shifts the elements after `i`, which costs O(n), and it can happen for up to n zeros.
* **Space Complexity:** O(1) - The array is modified in place, using only two index variables.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Turns `[1, 0, 2, 3, 0, 4, 5, 0]` into `[1, 0, 0, 2, 3, 0, 0, 4]`.
* Example 2: Leaves `[1, 2, 3]` unchanged.
* All zeros: The array stays all zeros with the same length.
* Zero at the last position: The zero is not duplicated.
* Zero before the last position: The copy takes the last position.
* Single element: Works with an array of one number.

### Expected Output

```text
test_all_zeros ... ok
test_example_one ... ok
test_example_two ... ok
test_single_element ... ok
test_zero_at_last_position ... ok
test_zero_before_last_position ... ok

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

* Runtime: **3 ms**
* Runtime percentile: **61.73%**
* Memory: **19.40 MB**
* Memory percentile: **33.29%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to modify an array in place while keeping its length fixed.
* How `insert` and `pop` can shift elements without building a new array.
* Why `insert` in the middle of a list costs O(n), making the whole solution O(n^2).
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
