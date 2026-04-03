# Create a Song class.
# A Song has
#  title
#  artist
#  duration seconds

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing

class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def get_duration_seconds(self):
        return self.duration_seconds
    
    def set_title(self, new_title):
        self.title = new_title
    def set_artist(self, new_artist):
        self.artist = new_artist
    def set_duration_seconds(self, new_duration_seconds):
        self.duration_seconds = new_duration_seconds

song1 = Song('Trumpets', 'Jason Derulo', 217)

print(song1.get_title())
print(song1.get_artist())
print(song1.get_duration_seconds())


# Changes to the title, artist and duraction_seconds of the Song
song1.set_title('Halo')
song1.set_artist('Beyonce')
song1.set_duration_seconds('261')
print(song1.get_title())
print(song1.get_artist())
print(song1.get_duration_seconds())