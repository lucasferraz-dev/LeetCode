import unittest

from solution import ListNode, Solution


def build_list(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


def to_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


class TestMiddleNode(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(self.solution.middleNode(head)), [3, 4, 5])

    def test_example_two(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(to_list(self.solution.middleNode(head)), [4, 5, 6])

    def test_single_node(self):
        head = build_list([1])
        self.assertEqual(to_list(self.solution.middleNode(head)), [1])

    def test_two_nodes(self):
        head = build_list([1, 2])
        self.assertEqual(to_list(self.solution.middleNode(head)), [2])

    def test_returns_same_node(self):
        head = build_list([1, 2, 3])
        self.assertIs(self.solution.middleNode(head), head.next)


if __name__ == "__main__":
    unittest.main()
