#playlist_test.py
import unittest
from playlist import Playlist
from song import Song 


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("MyPlaylist")

    def tearDown(self):
        pass

    def test_add_song(self):
        song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 356, 320 )
        self.playlist.add_song(song)
        self.assertTrue(song in self.playlist.collection)

    def test_remove_song(self):
        song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 356, 320 )
        song1 = Song("Sweet Child O'mine1", "Guns N' Roses1", "Appetite for Destruction1", 4, 300, 120 )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song1)
        self.playlist.remove_song(song)
        self.assertTrue(song not in self.playlist.collection) 
        self.assertTrue(song1 in self.playlist.collection) 

    def test_total_length(self):#in seconds
        song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 360, 320 )
        song1 = Song("Sweet Child O'mine1", "Guns N' Roses1", "Appetite for Destruction1", 4, 306, 120 )
        self.playlist.add_song(song)
        self.playlist.add_song(song1)
        result = self.playlist.total_length()
        self.assertEqual(666,result)

    def test_remove_disrated(self):
        song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 360, 320 )
        song1 = Song("Sweet Child O'mine1", "Guns N' Roses1", "Appetite for Destruction1", 2, 306, 120 )
        self.playlist.add_song(song)
        self.playlist.add_song(song1)
        self.playlist.remove_disrated(3)
        self.assertTrue(song1 not in self.playlist.collection)

    def test_remove_bad_quality(self):
        song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 360, 320 )
        song1 = Song("Sweet Child O'mine1", "Guns N' Roses1", "Appetite for Destruction1", 2, 306, 120 )
        self.playlist.add_song(song)
        self.playlist.add_song(song1)
        self.playlist.remove_bad_quality()
        self.assertTrue(song1 not in self.playlist.collection)

    def test_show_artist(self):
        song = Song("Sweet Child O'mine", "Guns N' Roses", "Appetite for Destruction", 5, 360, 320 )
        song1 = Song("Sweet Child O'mine1", "Guns N' Roses", "Appetite for Destruction1", 2, 306, 120 )
        self.playlist.add_song(song)
        self.playlist.add_song(song1)
        self.assertEqual(["Guns N' Roses"], self.playlist.show_artist())




if __name__ == '__main__':
    unittest.main()