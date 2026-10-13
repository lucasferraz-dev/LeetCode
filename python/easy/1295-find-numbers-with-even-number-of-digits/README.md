# 1295 - Find Numbers with Even Number of Digits

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given an array `nums` of integers, return how many of them contain an even number of digits.

## My Approach

For each number, I count its digits by repeatedly dividing it by 10 with integer division (`//= 10`). Each division removes the last digit, so the number of divisions until it reaches 0 is the number of digits.

If the digit count is even (`cont % 2 == 0`), I increase the `even` counter. At the end, `even` holds the answer.

## Solution

```python
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even = 0
        for num in nums:
            cont = 0
            while num > 0:
                cont += 1
                num //= 10
            if cont % 2 == 0:
                even += 1
        return even
```

## Alternative: Using `len(str(num))`

The digit count can also be found by converting the number to a string and taking its length:

```python
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(len(str(num)) % 2 == 0 for num in nums)
```

It is shorter and easier to read. The division approach avoids creating strings and shows how to work with digits using math only.

## Complexity

* **Time Complexity:** O(n * d) - For each of the `n` numbers, the loop runs once per digit `d`. Since `nums[i] <= 10^5`, `d` is at most 6, so in practice it is O(n).
* **Space Complexity:** O(1) - Only two counters are used.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns `2` for `[12, 345, 2, 6, 7896]`.
* Example 2: Returns `1` for `[555, 901, 482, 1771]`.
* Single digits: Returns `0` when every number has one digit.
* All even: Returns the full length when every number has an even digit count.
* Upper bound: Counts `100000` (6 digits) correctly.

### Expected Output

```text
test_all_even ... ok
test_example_one ... ok
test_example_two ... ok
test_single_digits ... ok
test_upper_bound ... ok

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

* Runtime: **3 ms**
* Runtime percentile: **43.14%**
* Memory: **19.36 MB**
* Memory percentile: **28.42%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to count the digits of a number using integer division by 10.
* How `len(str(num))` gives the same result in a shorter way.
* How to check if a number is even with the modulo operator.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
