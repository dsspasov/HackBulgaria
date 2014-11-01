# MusivPlayer.py
from song import Song


from playlist import Playlist


from MusicCrawler import MusicCrawler


class MusicPlayer:

    def __init__(self):
        self.playlist = Playlist("myPlaylist")
        self.choice = 0

    def list_options(self):
        options = ["craw a directory (<path_to_the_files>)",
                   "create empty playlist(<name_of_the_playlist>)",
                   "load a playlist(<name_of_the file_to_load_from>)",
                   "save a playlist(<name_of_the_file_to_save_in>)",
                   "add song to a playlist(<song>)",
                   "remove song from the playlist()(<song>)",
                   "remove disrated songs(<rating>)",
                   "remove songs with bad quality",
                   "show artists",
                   "print",
                   "list options",
                   "finish"]
        for index, value in enumerate(options):
            print (index + 1, value)
        print("<song> is <title> <artist> <album> <rating> <length> <bitrate>")

    def options(self, args):
        if (self.choice == 1):
            self.playlist = MusicCrawler(args[0]).generate_playlist()
        elif(self.choice == 2):
            self.playlist = Playlist(args[0])
        elif(self.choice == 3):
            self.playlist = Playlist.load(args[0])
        elif(self.choice == 4):
            self.playlist.save(args[0])
        elif(self.choice == 5):
            song = Song(args[0], args[1], args[2], int(
                args[3]), int(args[4]), int(args[5]))
            self.playlist.add_song(song)
        elif(self.choice == 6):
            song = Song(args[0], args[1], args[2], int(
                args[3]), int(args[4]), int(args[5]))
            self.playlist.remove_song(song)
        elif(self.choice == 7):
            self.playlist.remove_disrated(int(args[0]))
        elif(self.choice == 8):
            self.playlist.remove_bad_quality()
        elif(self.choice == 9):
            print(self.playlist.show_artist())
        elif(self.choice == 10):
            print(self.playlist)
        elif(self.choice == 11):
            self.list_options()
        else:
            print("Enter a valid command")

    def user_decision(self):
        self.list_options()
        while True:

            command = input("Enter command>")
            command = command.split(" ")
            self.choice = int(command[0])
            arguments = command[1:]
            if self.choice == 12:
                break
            else:
                self.options(arguments)


def main():
    player = MusicPlayer()
    player.user_decision()


if __name__ == '__main__':
    main()
