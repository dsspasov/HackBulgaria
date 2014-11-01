#song.py


class Song:
    #MAX_RATING = 5
    #MIN_RATING = 0
    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def get_length(self):
        return self.length

    def rate(self, number):
        if number in range(0, 6):
            self.rating = number
        else:
            raise ValueError
