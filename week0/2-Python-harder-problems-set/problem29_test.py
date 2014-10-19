#problem29_test.py
import unittest
from problem29 import unique_words_count

class Test_Unique_Word_Count(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(0,unique_words_count([]))
    def test_not_empty_with_different_element(self):
        self.assertEqual(3,unique_words_count(["apple", "banana","banana", "apple", "pie"]))
    def test_not_empty_with_not_different_element(self):
        self.assertEqual(1, unique_words_count(["banana","banana"]))


if __name__ == '__main__':
    unittest.main()
