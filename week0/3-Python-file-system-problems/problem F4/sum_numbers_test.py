#sum_numbers_test.py
import unittest
from sum_numbers import get_content,sum_num

import os

class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.text = '1 2 3 4 5 6'
        self.file = open(self.filename,'w')
        self.file.write(self.text)
        self.file.close()
    def tearDown(self):
        os.remove(self.filename)
    def test_get_content(self):
        self.assertEqual(['1','2','3','4','5','6'],get_content(self.filename))
    def test_sum_num(self):
        self.assertEqual(21,sum_num(['1','2','3','4','5','6']))
if __name__ == '__main__':
    unittest.main()