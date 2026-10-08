# 0383 - Ransom Note

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

## My Approach

My first attempt used three `for` loops. It was more complicated than needed, so I rewrote it using a dictionary to count the letters.

The idea is to treat `magazine` as a stock of letters:

* First, I go through `magazine` and count how many times each letter appears, storing it in the dictionary `seen`. `seen.get(i, 0) + 1` starts the count at `0` for letters that were not seen yet.
* Then, I go through `ransomNote` and use one letter from the stock for each character, decreasing its count by `1`.
* If a letter is not in `seen`, or its count is already `0`, there are not enough letters in `magazine`, so I return `False` right away.

If every letter of `ransomNote` was found in the stock, I return `True`.

## Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}

        for i in magazine:
            seen[i] = seen.get(i,0) + 1

        for i in ransomNote:
            if i in seen and seen[i] > 0:
                seen[i] -= 1
            else:
                return False
        return True
```

### Alternative Solution (set + count)

This problem can also be solved with `set` and `count`. For each distinct letter of `ransomNote`, I check if it appears in `magazine` at least as many times as it appears in `ransomNote`:

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True
```

It is shorter, but each `count` goes through the whole string again. Since there are at most 26 distinct lowercase letters, it is still linear in practice.

## Complexity

* **Time Complexity:** O(m + n) - `magazine` (size `m`) and `ransomNote` (size `n`) are each traversed once.
* **Space Complexity:** O(1) - The dictionary stores at most 26 keys, one for each lowercase English letter, regardless of the size of the strings.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `False` when the letter is not in `magazine`.
* Example 2: Returns `False` when `magazine` does not have enough copies of a letter.
* Example 3: Returns `True` when `magazine` has enough copies of every letter.
* Same strings: Returns `True` when both strings are equal.
* Different order: Returns `True` when the letters are in a different order in `magazine`.
* Ransom note longer: Returns `False` when `ransomNote` is longer than `magazine`.

### Expected Output

```text
test_different_order ... ok
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_ransom_note_longer ... ok
test_same_strings ... ok

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

* Runtime: **23 ms**
* Runtime percentile: **54.11%**
* Memory: **19.46 MB**
* Memory percentile: **94.36%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to use a dictionary as a counter of available letters.
* How to use `dict.get` with a default value to count occurrences.
* How to simplify a solution with nested loops into two separate passes.
* How the same problem can be solved with `set` and `count`.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
