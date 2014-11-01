# playlist.py

from song import Song

import json


class Playlist:

    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_song(self, song):

        self.collection.append(song)

    def remove_song(self, song):
        temp_list = []
        for each_song in self.collection:
            if ((each_song.title == song.title) and
                (each_song.artist == song.artist) and
                (each_song.album == song.album) and
                (each_song.rating == song.rating) and
                (each_song.length == song.length) and
                    (each_song.bitrate == song.bitrate)):
                continue
            else:
                temp_list.append(each_song)
        self.collection.clear()
        self.collection = temp_list.copy()

    # return total length of all song in seconds
    def total_length(self):
        length = 0
        for each_song in self.collection:
            length += each_song.get_length()
        return length

    def remove_disrated(self, rating):
        temp_list = []
        for each_song in self.collection:
            if each_song.rating <= rating:
                continue
            else:
                temp_list.append(each_song)
        self.collection.clear()
        self.collection = temp_list.copy()

    def remove_bad_quality(self):
        temp_list = []
        for each_song in self.collection:
            if each_song.bitrate <= 150:
                continue
            else:
                temp_list.append(each_song)
        self.collection.clear()
        self.collection = temp_list.copy()

    def show_artist(self):
        temp_list = []
        for each_song in self.collection:
            if each_song.artist not in temp_list:
                temp_list.append(each_song.artist)
            else:
                continue

        return temp_list

    def convert_seconds_to_str_minutes(self, seconds):
        m = 0
#        s = 0
        while seconds >= 60:
            m += 1
            seconds -= 60
        return (str(m) + ':' + str(seconds))

    def __str__(self):
        result = ""
        for each_song in self.collection:
            result = result + each_song.artist + " " + each_song.title +\
                " - " + \
                self.convert_seconds_to_str_minutes(each_song.length) + "\n"
        return result

    def save(self, file_name):
        songs = []
        for each_song in self.collection:
            # songs.append({"title":each_song.title,
            #    "artist":each_song.artist,
            #    "album":each_song.album,
            #    "rating":each_song.rating,
            #    "length":each_song.length,
            #    "bitrate":each_song.bitrate})
            songs.append(each_song.__dict__)
        jsondata = {
            "name": self.name,
            "songs": songs
        }
        result = json.dumps(jsondata, indent=4)
        fd = open(file_name, 'w')
        fd.write(result)
        fd.close()

    def load(file_name):
        returndata = {}
        fd = open(file_name, 'r')
        text = fd.read()
        fd.close()
        returndata = json.loads(text)
        playlist = Playlist(returndata['name'])
        playlist = Playlist(returndata['name'])
        for each_song in returndata['songs']:
            song = Song(each_song['title'], each_song['artist'], each_song[
                        'album'], each_song['rating'], each_song[
                        'length'], each_song['bitrate'])
            playlist.add_song(song)
        return playlist


def main():
    playlist = Playlist("MyPlaylist")
    song = Song("Sweet Child O'mine", "Guns N' Roses",
                "Appetite for Destruction", 5, 360, 320)
    song1 = Song(
        "Sweet", "Guns N' Roses", "Appetite for Destruction1", 2, 306, 120)
    playlist.add_song(song)
    playlist.add_song(song1)

    playlist.save('my_json.json')
    rs = Playlist.load('my_json.json')

    print(rs)
if __name__ == '__main__':
    main()
