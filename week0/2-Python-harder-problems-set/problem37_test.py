#problem37_test.py
import unittest
from problem37 import member_of_nth_fib_lists

class TestMemberOfFibList(unittest.TestCase):
    def test_for_False(self):
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    def test_for_True(self):
        self.assertTrue(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
if __name__ == '__main__':
    unittest.main()