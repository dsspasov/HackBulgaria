#problem34_test.py
import unittest
from problem34 import simplify_fraction

#setUp(self):
#tearDown(self)
class TestSimplyfyFraction(unittest.TestCase):
    def test_division_by_0(self):
        self.assertFalse(simplify_fraction((1,0)))
    def test_if_numerator_is_zero(self):
        self.assertEqual((0,1),simplify_fraction((0,7)))
    def test_fraction_that_can_not_be_simplified(self):
        self.assertEqual((1,7),simplify_fraction((1,7)))
    def test_simplifing_fraction(self):
        self.assertEqual((1,3),simplify_fraction((3,9)))


if __name__ == '__main__':
    unittest.main()
