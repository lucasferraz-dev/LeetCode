# 0009 - Palindrome Number

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward.

**Follow up:** Could you solve it without converting the integer to a string?

## My Approach

My first solution converted `x` to a string and compared it with its reverse using `[::-1]`. It worked, but the problem asks to try solving it without converting the integer to a string, so I rewrote it using only math operations.

First, I noticed that any negative number can never be a palindrome, because the minus sign only appears at the beginning. For example, `-121` read backward is `121-`. So if `x < 0`, I return `False` right away.

For non-negative numbers, I build the reversed number digit by digit:

* `x % 10` gets the last digit of `x`.
* `reversedNum * 10 + digit` appends that digit to the end of the reversed number.
* `x //= 10` removes the last digit from `x`.

I keep a copy of the original value in `original`, because `x` is reduced to `0` during the loop. At the end, the number is a palindrome if the reversed number is equal to the original.

## Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum = 0
        original = x
        if x < 0:
            return False
        while x > 0:
            digit = x % 10
            reversedNum = reversedNum * 10 + digit
            x //= 10
        return reversedNum == original
```

### First Solution (with string)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```

## Complexity

* **Time Complexity:** O(log n) - The loop runs once for each digit of `x`, and a number `n` has about log10(n) digits.
* **Space Complexity:** O(1) - Only a few integer variables are used, regardless of the size of `x`.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `True` for a palindrome number.
* Example 2: Returns `False` for a negative number.
* Example 3: Returns `False` for a number ending in `0`.
* Zero: Returns `True` for `0`.
* Single digit: Returns `True` for a number with only one digit.
* Even length palindrome: Returns `True` for a palindrome with an even number of digits.

### Expected Output

```text
test_even_length_palindrome ... ok
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_single_digit ... ok
test_zero ... ok

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
* Runtime percentile: **89.17%**
* Memory: **19.21 MB**
* Memory percentile: **55.19%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to solve a problem with math instead of converting the number to a string.
* How to extract the last digit of a number with `% 10` and remove it with `// 10`.
* How to build a reversed number digit by digit.
* Why negative numbers can never be palindromes.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
