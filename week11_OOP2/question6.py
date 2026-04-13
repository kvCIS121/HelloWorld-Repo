class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def get_artist(self):
        return self.artitst
    
    def set_artist(self, new_artist):
        self.artist = new_artist
    
    def play(self):
        print(f'Title: {self.title}, Artist: {self.artist}')
    
    def __str__(self):
        return f'Song(title = {self.title}, artist = {self.artist})'

class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
    
    def play_all(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        return f'Playlist(playlist_name = {self.playlist_name})'

song_1 = Song('Trumpets', 'Jason Derulo')
song_2 = Song('Interstellar OST', 'Hans Zimmer')

playlist_1 = Playlist('My music playlist')

playlist_1.add_song(song_1)
playlist_1.add_song(song_2)

playlist_1.play_all()
print(playlist_1)