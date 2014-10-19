#problem28_test.py
import unittest
from problem28 import count_words

class TestWordCount(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual({},count_words({}))
    def test_not_empty_dict_with_different_elements(self):
        result = count_words(["apple", "banana", "apple", "pie"])
        self.assertEqual({'pie': 1, 'banana': 1, 'apple': 2},result)
    def test_not_empty_dict_with_equal_element(self):
        result = count_words(['a', 'a', 'a', 'a', 'a'])
        self.assertEqual({'a' : 5}, result)
if __name__ == '__main__':
    unittest.main()
