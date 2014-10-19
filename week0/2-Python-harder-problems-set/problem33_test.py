#problem33_test.py
import unittest

from problem33 import is_an_bn

class TestA_eq_B(unittest.TestCase):
    def test_if_str_is_empty(self):
        self.assertTrue(is_an_bn(""))
    def test_if_a_eq_b(self):
        self.assertTrue(is_an_bn("aabb"))
    def test_if_a_neq_b(self):
        self.assertFalse(is_an_bn("aaabb"))
if __name__ == '__main__':
    unittest.main()