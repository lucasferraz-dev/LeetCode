# 2974 - Minimum Number Game

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

You are given a 0-indexed integer array `nums` of even length and there is also an empty array `arr`. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

* Every round, first Alice will remove the minimum element from `nums`, and then Bob does the same.
* Now, first Bob will append the removed element in the array `arr`, and then Alice does the same.
* The game continues until `nums` becomes empty.

Return the resulting array `arr`.

## My Approach

Since each round always removes the two smallest elements, I sort the array first. After sorting, every round is just one pair of neighbours: `nums[i]` (Alice's number) and `nums[i+1]` (Bob's number).

I go through the sorted array two positions at a time:

* Bob appends first, so I append `nums[i+1]`.
* Then Alice appends, so I append `nums[i]`.

In the end, `res` is the sorted array with every pair swapped.

## Solution

```python
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 2):
            res.append(nums[i+1])
            res.append(nums[i])
        return res
```

## Complexity

* **Time Complexity:** O(n log n) - Sorting dominates; the loop after it is O(n).
* **Space Complexity:** O(n) - The result array stores all `n` elements.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `[3, 2, 5, 4]` for `[5, 4, 2, 3]`.
* Example 2: Returns `[5, 2]` for `[2, 5]`.
* Already sorted: Swaps every pair of a sorted array.
* Reverse sorted: Sorts first and then swaps every pair.
* Duplicates: Works when the same number appears more than once.

### Expected Output

```text
test_already_sorted ... ok
test_duplicates ... ok
test_example_one ... ok
test_example_two ... ok
test_reverse_sorted ... ok

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

* Runtime: **0 ms**
* Runtime percentile: **100.00%**
* Memory: **19.22 MB**
* Memory percentile: **64.15%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How sorting can turn a simulation into a simple pass over the array.
* How to iterate two positions at a time with `range(0, len(nums), 2)`.
* How to swap pairs while building a new list.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
