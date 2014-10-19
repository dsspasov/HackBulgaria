#problem32_test.py
import unittest

from problem32 import reduce_file_path


class TestReduceFilePath(unittest.TestCase):

    def test_with_empty_string(self):
        self.assertEqual("/", reduce_file_path(""))

    def test_with_one_slash(self):
        self.assertEqual("/",reduce_file_path("/"))

    def test_only_with_slashes(self):
        self.assertEqual("/",reduce_file_path("////////////////"))

    def test_with_going_back_one_directory(self):
        self.assertEqual("/",reduce_file_path("/../"))

    def test_with_going_back_one_directory_and_lots_of_folders(self):
        self.assertEqual("/", reduce_file_path("/etc1/../etc2/../etc3/../etc4/../etc5/../etc6/../"))

    def test_with_staying_in_the_same_directory(self):
        self.assertEqual("/srv", reduce_file_path("/srv/./././././"))

    def test_with_two_slashes(self):
        self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))

    def test_full(self):
        self.assertEqual("/hack/week0/problem32.py",reduce_file_path("/hack//week0/.././week0//problem32.py/"))

    def test_already_reduced(self):
        self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf"))

if __name__ == '__main__':
    unittest.main()