#concat_files_test.py
import unittest
from concat_files import get_content,file_put

import os
from random import randint

class TestConcatenationFiles(unittest.TestCase):

    def setUp(self):
        self.number_of_files = randint(1,4)
        self.files = []
        self.content =[]
        self.concatenated = ''
        for i in range(self.number_of_files):

            self.text = 'this is a test'+str(i)
            self.content.append(self.text)
            self.concatenated += self.text
            #num = str(i)

            self.filename = "test%s.txt" %(i) 
            self.files.append(self.filename)

            self.file = open(self.filename,'w')
            self.file.write(self.text)

            self.file.close()

    def tearDown(self):
        for self.each_file in self.files:
            os.remove(self.each_file)

        self.fileMegatron = open("MEGATRON.txt",'w')
        self.fileMegatron.write('')
        self.fileMegatron.close()


    def test_if_content_is_get_from_files(self):
        for index in range(len(self.files)):
            self.assertEqual(self.content[index], get_content(self.files[index]))

    def test_if_content_is_put_in_a_file(self):
        for index in range(len(self.files)):
            file_put(self.content[index])
        self.assertEqual(self.concatenated, get_content("MEGATRON.txt"))


if __name__ == '__main__':
    unittest.main()

