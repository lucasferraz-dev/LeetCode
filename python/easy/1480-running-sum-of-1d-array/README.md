# 1480 - Running Sum of 1d Array

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given an array `nums`, we define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

## My Approach

My first solution used a counter to accumulate the sum. At each index `i`, I added `nums[i]` to the counter and appended its current value to a new result list.

That approach worked, but it created an additional list of the same size as the input.

To improve the space complexity, I decided to modify the input list itself. Starting from index `1`, each element receives its own value plus the previous element, which already holds the running sum up to that point.

This way, the list is transformed in place and no extra list is needed.

## Solution

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
```

## Complexity

* **Time Complexity:** O(n) — Each element is visited once.
* **Space Complexity:** O(1) auxiliary space — The running sum is stored directly in the input list, without creating an additional list.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Calculates the running sum of increasing values.
* Example 2: Handles an array containing only identical values.
* Example 3: Validates the result with mixed values.
* Single element: Validates the result when the array contains only one number.

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

* Runtime: **X ms**
* Runtime percentile: **X%**
* Memory: **X MB**
* Memory percentile: **X%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to calculate a running sum using the previous element as an accumulator.
* How modifying the input list in place can reduce auxiliary space complexity.
* How to start a loop from index `1` to safely access the previous element.
* How to analyze time and auxiliary space complexity.
* How to validate solutions using automated unit tests.
