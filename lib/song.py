import ipdb

# from song import Song

# Song.count = 0
# Song.genre_count = {}
# Song.artist_count = {}


# FAILED Class "Song" in song.py counts the total number of Song objects. - assert 0 == 4

# FAILED Class "Song" in song.py keeps track of all Song genres. - AssertionError: assert 'Rap' in []

# FAILED Class "Song" in song.py keeps track of all Song artists. - AssertionError: assert 'Jay Z' in []

# FAILED Class "Song" in song.py keeps count of Songs for each genre. - KeyError: 'Rap'

# FAILED Class "Song" in song.py keeps count of Songs for each artist. - KeyError: 'Jay Z'

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        
        

#class methods

# Your `__init__` method should call a class method
# `add_song_to_count()` that increments the value of `count` by one.

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    

# Next, define the following class methods:
# `add_to_genres()`: adds any new genres to a class attribute `genres`

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)



# `add_to_artists()`: adds any new artists to a class attribute `artists`

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

  
# we write our `add_to_artist_count()` method.

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# `add_to_genre_count()`: adds to a class attribute `genre_count`, a dictionary
# in which the keys are the names of each genre. Each genre name key should point
# to a value that is the number of songs that have that genre.

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    


song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
song4 = Song("Out of Touch", "Hall and Oates", "Pop")  
song5 = Song("Sara Smile", "Hall and Oates", "Pop")

# ipdb.set_trace()
