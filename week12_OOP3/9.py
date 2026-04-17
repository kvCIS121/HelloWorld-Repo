class Playlist:
    def __init__(self, name='New Playlist', songs=None):
        self.name = name
        self.songs = songs if songs is not None else []
        
    def add_song(self, song):
        self.songs.append(song)
    
    def __add__(self, other):
        new_name = self.name + other.name
        new_songs = self.songs + other.songs
        return Playlist(new_name, new_songs)
    
    def __str__(self):
        return f'Playlist(name = {self.name}, songs = {self.songs})'

# Creating playlist objects
p1 = Playlist("Chill Vibes", ["Late Night Drive", "Soft Lights", "Ocean Breeze"])
p2 = Playlist("Workout Mix", ["Pump It Up", "Run Faster"])
p3 = Playlist("Anime OST", ["Unravel", "Guren no Yumiya", "Again"])
p4 = Playlist("Jazz Classics", ["Autumn Leaves", "Blue in Green"])
p5 = Playlist("New Playlist", [])   # uses default name, empty songs

new_playlist_1 = p1 + p2
print(new_playlist_1)


# Print readable playlists
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)