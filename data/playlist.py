# playlist.py
# Contains Song and Playlist classes


class Song:
    """
    Represents a song with name, singer, and genre.
    """

    def __init__(self, name, singer, genre):
        self.name = name
        self.singer = singer
        self.genre = genre

    def __str__(self):
        return f"{self.name} by {self.singer} ({self.genre})"
class Playlist:
    """
    Represents a playlist containing multiple songs.
    """

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        """Adds a song to the playlist."""
        self.songs.append(song)

    def remove_song(self, song_name):
        """Removes a song from the playlist by name."""
        for song in self.songs:
            if song.name.lower() == song_name.lower():
                self.songs.remove(song)
                return True
        return False

    def rename(self, new_name):
        """Renames the playlist."""
        self.name = new_name

    def has_song(self, song_name):
        """Checks if a song exists in the playlist."""
        return any(song.name.lower() == song_name.lower() for song in self.songs)

    def __str__(self):
        if not self.songs:
            return f"{self.name}: (No songs)"
        song_list = ", ".join(str(song) for song in self.songs)
        return f"{self.name}: {song_list}"
