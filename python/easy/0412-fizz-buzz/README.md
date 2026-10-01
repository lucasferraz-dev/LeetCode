# 0412 - Fizz Buzz

**Difficulty:** Easy
**Language:** Python
**Status:** Accepted

## Problem

Given an integer `n`, return a string array where:

* Multiples of 3 are `"Fizz"`
* Multiples of 5 are `"Buzz"`
* Multiples of both 3 and 5 are `"FizzBuzz"`
* All other numbers are converted to strings

---

## My Approach

I used a single `for` loop to go through all numbers from `1` to `n`.

For each number, I check its divisibility using the modulo operator `%`.

### FizzBuzz condition

Initially, I considered checking divisibility by 3 and 5 separately:

```python
if i % 3 == 0 and i % 5 == 0:
```

I realized that a number divisible by both 3 and 5 is also divisible by 15, so I changed it to:

```python
if i % 15 == 0:
```

This makes the condition more direct.

### Converting numbers to strings

For numbers that are not divisible by 3 or 5, the problem requires a string.

I used:

```python
str(i)
```

to convert the integer into a string.

---

## Solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []

        for i in range(1, n + 1):

            if i % 15 == 0:
                answer.append("FizzBuzz")

            elif i % 3 == 0:
                answer.append("Fizz")

            elif i % 5 == 0:
                answer.append("Buzz")

            else:
                answer.append(str(i))

        return answer
```

---

## Complexity

* **Time:** O(n)
* **Space:** O(n)

The loop runs once for every number from `1` to `n`.

The `answer` list contains `n` elements, so the space complexity is O(n).

---

## Running Tests

The solution includes a separate test file, `test_solution.py`, containing automated test cases implemented with Python's built-in `unittest` framework.

### Execute the tests

From the exercise directory, run:

```bash
python -m unittest -v
```

### Test coverage

The test suite checks:

* Example 1: `n = 3`
* Example 2: `n = 5`
* Example 3: `n = 15`
* Additional case: `n = 30`, verifying the final `"FizzBuzz"` result.

### Expected output

```text
test_example_one ... ok
test_example_two ... ok
test_example_three ... ok
test_fizzbuzz_multiple ... ok

----------------------------------------------------------------------
Ran 4 tests

OK
```

All tests must pass for the solution to be considered correct against these test cases.

The tests can also be executed directly using:

```bash
python test_solution.py
```

---

## LeetCode Result

**65 / 65 test cases passed** 

* Runtime: **1 ms**
* Runtime percentile: **34.66%**
* Memory: **19.66 MB**
* Memory percentile: **17.76%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

---

## What I Learned

* Using `%` to check divisibility.
* Why checking `i % 15` handles numbers divisible by both 3 and 5.
* Converting integers to strings using `str()`.
* Understanding that O(n) is optimal here because the problem requires generating one result for every number from `1` to `n`.
