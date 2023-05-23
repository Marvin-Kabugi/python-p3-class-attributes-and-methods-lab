class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artist(self)
        Song.counts_genre(self)
        Song.counts_artist(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if not song.genre in cls.genres:
            cls.genres.append(song.genre)

    @classmethod
    def add_to_artist(cls, song):
        if not song.artist in cls.artists:
            cls.artists.append(song.artist)

    @classmethod
    def counts_genre(cls, song):
        cls.genre_count[song.genre] = 1 + cls.genre_count.get(song.genre, 0)

    @classmethod
    def counts_artist(cls, song):
        cls.artist_count[song.artist] = 1 + cls.artist_count.get(song.artist, 0)

