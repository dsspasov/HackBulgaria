#problem38_test.py
import unittest
from problem38 import goldbach

class TestGoldBach(unittest.TestCase):
    def test_for_one_result(self):
        self.assertEqual([(2,2)], goldbach(4))
    def test_for_two_results(self):
        self.assertEqual([(3,7), (5,5)], goldbach(10))
    def test_for_more_results(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))

if __name__ == '__main__':
    unittest.main()
        