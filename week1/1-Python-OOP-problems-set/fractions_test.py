#fractions_test.py
import unittest
from fractions import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.first = Fraction(1,2)
        self.second = Fraction(2,2)
    def tearDown(self):
        pass
    def test_add(self):
        #first = Fraction(1,1)
        #second = Fraction(2,2)
        self.assertEqual(Fraction(6,4),(self.first+self.second))
    def test_sub(self):
        self.assertEqual(Fraction(-2,4),(self.first-self.second))
    def test_mul(self):
        self.assertEqual(Fraction(2,4),(self.first*self.second))
    def test_equal(self):
        self.assertTrue((Fraction(1,2)==Fraction(1,2)))
        self.assertFalse(self.first == self.second)
    def test_gt(self):
        self.assertTrue(((Fraction(1,1)>Fraction(1,2))))
        self.assertFalse(((Fraction(1,5)>Fraction(1,1))))
    def test_lt(self):
        self.assertTrue(((Fraction(1,2)<Fraction(1,1))))
        self.assertFalse(((Fraction(1,1)<Fraction(1,5))))

if __name__ == '__main__':
    unittest.main()