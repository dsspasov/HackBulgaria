#generate_numbers_test.py
import unittest

from generate_numbers import generate_numbers
from concat_files import get_content

import os
from random import randint

class TestGenerateNumbers(unittest.TestCase):

    def setUp(self):
        self.filename = "test.txt"
        self.amount_of_numbers = randint(1,10)

        content = []
        for i in range(self.amount_of_numbers):
            content.append(str(randint(1,1000)))
        file = open(self.filename,"w")
        file.write(" ".join(content))
        file.close()

    def tearDown(self):
        os.remove(self.filename)

    def test_amount_of_numbers(self):
        content = get_content(self.filename)
        content = content.split(" ")
        self.assertEqual(len(content), self.amount_of_numbers)

if __name__ == '__main__':
    unittest.main()

