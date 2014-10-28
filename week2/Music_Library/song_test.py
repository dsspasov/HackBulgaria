#song_test.py
import unittest
from song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 356, 320 )

    def test_rate_0(self):
        self.song.rate(5)
        self.assertEqual(5,self.song.rating)
    def test_rate_error(self):
        self.assertRaises(ValueError, lambda:self.song.rate(6))
        #with self.assertRaises(ValueError):
        #    self.song_rate(6)


if __name__ == '__main__':
    unittest.main()