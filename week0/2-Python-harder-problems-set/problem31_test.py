#problem31_test.py
import unittest
from problem31 import prepare_meal

class TestPrepareMeal(unittest.TestCase):
    def test_with_0(self):
        self.assertEqual("Empty",prepare_meal(0))
    def test_with_not_0(self):
        self.assertEqual("spam and eggs ",prepare_meal(15))
    def test_with_not_divisable_by_3_or_5(self):
        self.assertEqual("Empty", prepare_meal(4))
    def test_with_divisible_by_3(self):
        self.assertEqual("spam spam ", prepare_meal(9))
    def test_with_divisible_by_5(self):
        self.assertEqual("eggs eggs ", prepare_meal(25))
if __name__ == '__main__':
    unittest.main()