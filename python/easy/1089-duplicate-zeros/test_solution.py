import unittest

from solution import Solution


class TestDuplicateZeros(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        self.solution.duplicateZeros(arr)
        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_example_two(self):
        arr = [1, 2, 3]
        self.solution.duplicateZeros(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_all_zeros(self):
        arr = [0, 0, 0, 0]
        self.solution.duplicateZeros(arr)
        self.assertEqual(arr, [0, 0, 0, 0])

    def test_zero_at_last_position(self):
        arr = [1, 2, 0]
        self.solution.duplicateZeros(arr)
        self.assertEqual(arr, [1, 2, 0])

    def test_zero_before_last_position(self):
        arr = [1, 0, 2]
        self.solution.duplicateZeros(arr)
        self.assertEqual(arr, [1, 0, 0])

    def test_single_element(self):
        arr = [0]
        self.solution.duplicateZeros(arr)
        self.assertEqual(arr, [0])


if __name__ == "__main__":
    unittest.main()
