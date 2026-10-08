# 0876 - Middle of the Linked List

**Difficulty:** Easy
**Language:** Python
**Status:** Solved

## Problem

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

## My Approach

My first solution went through the list once with a counter `cont` to find its length. Then I divided `cont` by `2` and walked from `head` again that number of steps to reach the middle node. It worked, but it needed two passes over the list.

Then I rewrote it using the fast and slow pointers technique, which finds the middle in a single pass:

* `slow` moves one node at a time.
* `fast` moves two nodes at a time.

Both start at `head`. Since `fast` moves twice as fast as `slow`, when `fast` reaches the end of the list, `slow` is exactly in the middle.

The loop runs while `fast` and `fast.next` both exist. This handles both cases:

* Odd length: `fast` stops on the last node, and `slow` is on the only middle node.
* Even length: `fast` becomes `None` after passing the last node, and `slow` is on the second middle node, which is the one the problem asks for.

## Solution

```python
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## Complexity

* **Time Complexity:** O(n) - `fast` goes through the list once, so the loop runs about n / 2 times.
* **Space Complexity:** O(1) - Only two pointers are used, regardless of the size of the list.

## Running Tests

I created a separate `test_solution.py` file using Python's built-in `unittest` framework. It has two helpers: `build_list` creates a linked list from a Python list, and `to_list` converts the returned node back to a Python list to compare the results.

Run the tests from the exercise directory:

```bash
python -m unittest -v
```

### Test Coverage

* Example 1: Returns the only middle node for a list with an odd length.
* Example 2: Returns the second middle node for a list with an even length.
* Single node: Returns the head when the list has only one node.
* Two nodes: Returns the second node.
* Same node: Returns the actual node from the list, not a copy.

### Expected Output

```text
test_example_one ... ok
test_example_two ... ok
test_returns_same_node ... ok
test_single_node ... ok
test_two_nodes ... ok

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
* Runtime percentile: **100%**
* Memory: **19.30 MB**
* Memory percentile: **59.36%**

> Runtime and memory measurements can vary between submissions. The main focus is the algorithmic complexity and reasoning behind the solution.

## What I Learned

* How to traverse a singly linked list.
* How to use the fast and slow pointers technique to find the middle in a single pass.
* Why the loop condition `fast and fast.next` returns the second middle node when the length is even.
* How to improve a two-pass solution into a one-pass solution.
* How to analyze time and space complexity.
* How to validate solutions using automated unit tests.
