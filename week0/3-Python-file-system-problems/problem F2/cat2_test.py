#cat2_test.py
import unittest
from cat2 import cat2

import os
from random import randint

class TestCat2(unittest.TestCase):

    def setUp(self):
        self.number_of_files = randint(0,4)
        self.files = []
        self.concatenated = ''
        for i in range(self.number_of_files):
            self.filename = "test%s.txt" %(i)
            self.files.append(self.filename)

            self.text = 'this is a test'+str(i)
            self.concatenated += self.text

            self.file = open(self.filename,'w')
            self.file.write(self.text)
            self.file.close()

    def tearDown(self):
        for self.each_file in self.files:
            os.remove(self.each_file)

    def test_if_is_concatenated_from_files(self):
        self.assertEqual(self.concatenated, cat2(self.files))

if __name__ == '__main__':
    unittest.main()

