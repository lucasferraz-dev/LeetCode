# 0977 - Squares of a Sorted Array

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## First Attempt: Square and Sort

My first idea was the straightforward one: square every number and sort the result.

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(num * num for num in nums)
```

It works, but sorting makes it O(n log n). The problem calls this trivial and challenges you to solve it in O(n), so I looked for a different approach.

## My Approach: Two Pointers

The array is already sorted, so the largest square is always at one of the ends: either the most negative number on the left or the largest positive number on the right.

I use two pointers, `left` at the start and `right` at the end, and fill the result array from the last position to the first:

* Compare `abs(nums[left])` and `abs(nums[right])`.
* The bigger one has the largest remaining square, so I put its square at position `i` and move that pointer inward.
* Repeat until every position is filled.

Each step places the next largest square, so the result ends up sorted with no sorting step.

## Solution

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] * nums[left]
                left += 1
            else:
                res[i] = nums[right] * nums[right]
                right -= 1
        return res
```

## Complexity

* **Time Complexity:** O(n) - Each element is visited exactly once by one of the pointers.
* **Space Complexity:** O(n) - The result array stores `n` squares (O(1) extra besides the output).

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `[0, 1, 9, 16, 100]` for `[-4, -1, 0, 3, 10]`.
* Example 2: Returns `[4, 9, 9, 49, 121]` for `[-7, -3, 2, 3, 11]`.
* All negative: Squares come out in reverse order and are placed correctly.
* All positive: Squares keep the original order.
* Single element: Works with an array of one number.

### Expected Output

```text
test_all_negative ... ok
test_all_positive ... ok
test_example_one ... ok
test_example_two ... ok
test_single_element ... ok

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

* Runtime: **10 ms**
* Runtime percentile: **58.37%**
* Memory: **20.98 MB**
* Memory percentile: **73.08%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How the trivial square-and-sort solution costs O(n log n).
* How the two pointers technique uses the sorted input to reach O(n).
* How filling the result array from the end avoids reversing it later.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
