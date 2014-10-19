#problem39_test.py
import unittest

from problem39 import magic_square


class TestMagicSquare(unittest.TestCase):

    def test_row_false(self):
        self.assertFalse(magic_square([[1,2],[3,4]]))

    def test_col_false(self):
        self.assertFalse(magic_square([[1,2],[3,4]]))

    def test_forward_diagonal_false(self):
        self.assertFalse(magic_square([[1,1,1],[0,0,3],[2,2,-1]]))

    def test_backward_diagonal_false(self):
        self.assertFalse(magic_square([[1,1,1],[3,0,0],[-1,2,2]]))

    def test_matrix_true(self):
        self.assertTrue(magic_square([[1,1],[1,1]]))

    def test_only_row_true(self):
        self.assertFalse(magic_square([[1,1],[2,0]]))

    def test_diagonals_true(self):
        self.assertFalse(magic_square([[1,3],[1,3]]))

if __name__ == '__main__':

    unittest.main()