# 1365 - How Many Numbers Are Smaller Than the Current Number

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given the array `nums`, for each `nums[i]`, find out how many numbers in the array are smaller than it.

Return the answer in an array.

## My Approach

My initial approach was to use a dictionary to count the frequency of each number.

However, I realized that comparing each number against all the distinct keys would still require repeated iterations.

To improve the solution, I used sorting and a dictionary to store the first position of each number in the sorted array.

Since the first occurrence of a number in the sorted array represents how many elements are smaller than it, I can use that position to obtain the answer.

Finally, I iterate through the original array and retrieve the corresponding values from the dictionary, preserving the original order.

## Solution

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordenado = sorted(nums)
        posicoes = {}

        for i, numero in enumerate(ordenado):
            if numero not in posicoes:
                posicoes[numero] = i

        res = []

        for numero in nums:
            res.append(posicoes[numero])

        return res
```

## Complexity

* **Time Complexity:** O(n log n) - Sorting takes O(n log n), while building the dictionary and generating the result take O(n).
* **Space Complexity:** O(n) - The sorted array, dictionary, and result require additional space.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Handles duplicate values and different numbers.
* Example 2: Validates the result with an unsorted array.
* Example 3: Handles an array containing only identical values.
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

* Runtime: **0 ms**
* Runtime percentile: **100.00%**
* Memory: **19.25 MB**
* Memory percentile: **62.40%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to use sorting to simplify comparison problems.
* How to use dictionaries to store and retrieve information efficiently.
* How `enumerate()` provides both indexes and values during iteration.
* Why preserving the first occurrence of a duplicated number is important.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
