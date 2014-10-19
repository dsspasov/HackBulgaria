#problem30_test.py
import unittest
from problem30 import groupby

class TestGroupBy(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual({'odd':0, 'even':0}, groupby(lambda x: 'odd' if x % 2 else 'even', []))
    def test_not_empty_list(self):
        self.assertEqual({'odd':[1,3,5,9] , 'even':[2,8,10,12]}, groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
if __name__ == '__main__':
    unittest.main()
