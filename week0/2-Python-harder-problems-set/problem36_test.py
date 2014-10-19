#problem36_test.py
import unittest
from problem36 import nth_fib_lists

class TestFibonacciLists(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual([1], nth_fib_lists([1], [2], 1))
    def test_for_2(self):
        self.assertEqual([2] , nth_fib_lists([1], [2], 2))
    def test_for_3(self):
        self.assertEqual([1, 2, 1, 3] , nth_fib_lists([1, 2], [1, 3], 3))
    def test_for_more(self):
        self.assertEqual([1, 2, 3, 1, 2, 3] , nth_fib_lists([], [1, 2, 3], 4))
    def test_with_empty(self):
        self.assertEqual([] , nth_fib_lists([], [], 33))
if __name__ == '__main__':
    unittest.main()