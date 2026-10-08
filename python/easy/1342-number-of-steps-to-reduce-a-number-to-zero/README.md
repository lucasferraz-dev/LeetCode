# 1342 - Number of Steps to Reduce a Number to Zero

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given an integer `num`, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by `2`, otherwise, you have to subtract `1` from it.

## My Approach

I simply simulate the process described in the problem, counting each step until the number reaches `0`.

I use a counter `cont` that starts at `0`, and while `num` is greater than `0`:

* If `num % 2 == 0`, the number is even, so I divide it by `2` with `num //= 2`.
* Otherwise, the number is odd, so I subtract `1` from it.
* In both cases, I add `1` to the counter, because each operation is one step.

When the loop ends, `num` is `0` and `cont` holds the total number of steps. If `num` is already `0`, the loop never runs and the answer is `0`.

## Solution

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cont = 0
        
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            cont += 1
        return cont
```

## Complexity

* **Time Complexity:** O(log n) - Each division by `2` removes one binary digit from `num`, and there is at most one subtraction between two divisions, so the loop runs at most about 2 * log2(n) times.
* **Space Complexity:** O(1) - Only one counter variable is used, regardless of the size of `num`.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Counts the steps for a number that alternates between even and odd.
* Example 2: Counts the steps for a power of two.
* Example 3: Counts the steps for a larger odd number.
* Zero: Returns `0` when the number is already zero.
* One: Returns `1` for a single subtraction.
* Power of two: Only divides by `2` until reaching `1`, then subtracts once.

### Expected Output

```text
test_example_one ... ok
test_example_three ... ok
test_example_two ... ok
test_one ... ok
test_power_of_two ... ok
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

* Runtime: **0 ms**
* Runtime percentile: **100%**
* Memory: **19.30 MB**
* Memory percentile: **25.34%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to simulate a process step by step with a `while` loop.
* How to check if a number is even or odd with `% 2`.
* Why repeatedly dividing by `2` gives a logarithmic number of steps.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
