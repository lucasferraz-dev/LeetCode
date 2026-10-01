# 0001 - Two Sum

**Difficulty:** Easy
**Language:** Python
**Status:** Accepted

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

---

## My Approach

### First attempt - O(n²)

My first solution used two `for` loops to compare each number with the others.

This worked, but resulted in **O(n²)** time complexity.

### Optimized approach - Hash Map

After studying dictionaries and hash tables, I realized that I could store the numbers I had already seen along with their indices.

For each number:

1. Calculate the value needed to reach the target:

```python
target - nums[i]
```

2. Check if this value already exists in the dictionary.

3. If it exists, return the stored index and the current index.

4. Otherwise, store the current number and its index.

### Solution

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]

            seen[nums[i]] = i

        return []
```

---

## Complexity

| Complexity | Result   |
| ---------- | -------- |
| Time       | **O(n)** |
| Space      | **O(n)** |

The dictionary allows the lookup to be done in **O(1) average time**, avoiding the need for a second loop.

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

* Example 1: `[2, 7, 11, 15]`, target = `9`
* Example 2: `[3, 2, 4]`, target = `6`
* Example 3: `[3, 3]`, target = `6`

### Expected output

```text
test_example_one ... ok
test_example_two ... ok
test_example_three ... ok

----------------------------------------------------------------------
Ran 3 tests

OK
```

All tests must pass for the solution to be considered correct against these test cases.

The tests can also be executed directly using:

```bash
python test_solution.py
```

---

## What I Learned

While rewriting this problem, I made a few mistakes that helped me understand the solution better.

* I initially forgot to iterate using `range(len(nums))`.
* I confused the current number with its index.
* I initially thought about returning `nums[i]`, but the problem requires the **indices**.
* I learned that the dictionary stores the number as the key and its index as the value:

```python
seen[nums[i]] = i
```

For example:

```text
nums = [2, 7, 11, 15]

seen = {
    2: 0,
    7: 1
}
```

So if the current number needs `2`, `seen[2]` gives me its index: `0`.

This was also my first exercise where I understood why replacing a nested loop with a hash map can reduce the complexity from **O(n²) to O(n)**.

---

## LeetCode Result

**65 / 65 test cases passed** 

* Runtime: **3 ms**
* Runtime percentile: **53.49%**
* Memory: **20.65 MB**
* Memory percentile: **7.40%**

> Runtime and memory measurements can vary between submissions. The main focus here is the algorithmic complexity and the reasoning behind the solution.

