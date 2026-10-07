# 0242 - Valid Anagram

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

## My Approach

Two strings are anagrams when they have exactly the same letters with the same number of occurrences.

First, I check if both strings have the same length. If they don't, they can't be anagrams, so I return `False` right away.

Then I use two dictionaries, `seenS` and `seenT`, to count how many times each character appears in `s` and in `t`. If the character is not in the dictionary yet, I add it with a count of `1`; otherwise, I increment its count.

At the end, I compare both dictionaries. If they are equal, every character appears the same number of times in both strings, so `t` is an anagram of `s`.

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS = {}
        seenT = {}

        for i in s:
            if i not in seenS:
                seenS[i] = 1
            else:
                seenS[i] += 1

        for j in t:
            if j not in seenT:
                seenT[j] = 1
            else:
                seenT[j] += 1

        return(seenS == seenT)
```

## Complexity

* **Time Complexity:** O(n) - Each string is traversed once, and dictionary operations take O(1) on average. Comparing the dictionaries is also linear in the number of distinct characters.
* **Space Complexity:** O(1) - The problem says the strings contain only lowercase English letters, so each dictionary stores at most 26 keys.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `True` when `t` is an anagram of `s`.
* Example 2: Returns `False` when the strings have different letters.
* Different lengths: Returns `False` when the strings have different lengths.
* Same letters, different counts: Returns `False` when the letters match but appear a different number of times.
* Single character: Returns `True` for two equal single-character strings.

### Expected Output

```text
test_different_lengths ... ok
test_example_one ... ok
test_example_two ... ok
test_same_letters_different_counts ... ok
test_single_character ... ok

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

* Runtime: **15 ms**
* Runtime percentile: **42.99%**
* Memory: **19.36 MB**
* Memory percentile: **76.20%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

Even though O(n) is the best possible time complexity for this problem (every character needs to be read at least once), the runtime percentile was lower. This happens because the counting is done with a Python loop, while faster submissions usually rely on built-in tools like `collections.Counter`, which do the same counting in C. The complexity is the same; only the constant factor changes.

## What I Learned

* How to use dictionaries to count character occurrences.
* How to check lengths first to return early when the strings can't be anagrams.
* How to compare two dictionaries directly with `==`.
* Why a solution with optimal complexity can still have a lower runtime percentile in Python.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
