# MusicCrawler.py
from song import Song
from playlist import Playlist

import os

from mutagen.mp3 import MP3


def get_files(path):
    music_files = []
    for file in os.listdir(path):
        if file.endswith(".mp3"):
            music_files.append(file)
    return music_files


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        playlist = Playlist("myPlaylist")
        files = get_files(self.path)
        for each_file in files:
            audio = MP3('music/' + str(each_file))
            song = Song(str(audio['TIT2']), str(audio['TPE1']), str(
                audio['TALB']), 5, int(audio.info.length), audio.info.bitrate)
            playlist.add_song(song)
        return playlist
    # def generate_playlist(self):

    # sudo apt-get install python3-pip
    # sudo pip3 install mutagen
    # pip3 freeze


def main():

    a = MusicCrawler("music")
    playlist = a.generate_playlist()
    playlist.save("my_second.json")
    print(playlist)
    # get_files("music")
    #audio = MP3("music/Sweet.mp3")
    #audio["title"] = "An example"
    # audio.pprint()
    # audio.save()
    #t1 = audio['TSSE']
    # t2 = audio['TALB']#album
    # t3 = audio['TIT2']#title
    # t4 = audio['TPE1']#artist
    # t5 = audio['TDRL']#year

    # print(audio.info.length)
    # audio.info.pprint()
    # print(t1)
    # print(t2)
    # print(t3)
    # print(t4)
    # print(t5)

if __name__ == '__main__':
    main()
