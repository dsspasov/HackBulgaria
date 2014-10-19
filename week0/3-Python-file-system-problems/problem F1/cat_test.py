#cat_test.py
import unittest
from cat import cat

import os

class TestCatFunction(unittest.TestCase):

    def setUp(self):
        self.filename = "test.txt"
        self.text = 'this is a test'
        self.file = open(self.filename,'w')
        self.file.write(self.text)
        self.file.close()

        #self.file = open(self.filename, "r")
        #self.content = self.file.read()
        #self.file.close()
    def tearDown(self):
        os.remove(self.filename)
        #pass

    def test_if_is_readen_from_file(self):
        self.assertEqual(self.text,cat(self.filename))

if __name__ == '__main__':
    unittest.main()





