# 1528 - Shuffle String

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

You are given a string `s` and an integer array `indices` of the same length. The string `s` will be shuffled such that the character at the `i-th` position moves to `indices[i]` in the shuffled string.

Return the shuffled string.

## My Approach

Each value in `indices` tells exactly where the character at the same position in `s` should go.

So I created a list of empty strings with the same length as `s`, which works as the final positions of the shuffled string.

Then I iterate through `s` and place each character `s[i]` directly at position `indices[i]` in the list.

Since strings in Python are immutable, I used a list to build the result and then converted it back to a string with `"".join()`.

## Solution

```python
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [""] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        res = "".join(res)
        return res
```

## Complexity

* **Time Complexity:** O(n) — Each character is placed once, and `join()` also takes O(n).
* **Space Complexity:** O(n) — The auxiliary list stores all `n` characters.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Restores a string with shuffled indices.
* Example 2: Handles indices that are already in order.
* Reversed indices: Validates the result when the indices are in reverse order.
* Single character: Validates the result when the string contains only one character.

### Expected Output

```text
test_example_one ... ok
test_example_two ... ok
test_reversed_indices ... ok
test_single_character ... ok

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

* How to use an array of indices to place elements directly in their final positions.
* Why strings in Python are immutable and how to use a list to build a new string.
* How to convert a list of characters into a string with `"".join()`.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
