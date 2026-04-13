class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series
    
    def get_series(self):
        return self.series
    
    def set_series(self, new_series):
        self.series = new_series
    
    def communicate(self):
        print('Beep-Bloop-Blop')

    def __str__(self):
        return f'Droid(designation={self.designation}, series={self.series})'

# String = text data stored in a variable
# print() = displays something on the screen
# __str__ → return a string
# communicate() / speak() → print something. this is an action

class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []
    
    def get_droids(self):
        return self.droids
    
    def add_droids(self, droid):
        self.droids.append(droid)
    
    def droids_communicate(self):
        for droid in self.droids:
            droid.communicate()

    def __str__(self):
        return f'Starship(name={self.name}, droids={len(self.droids)})'
    
droid_1 = Droid('R2D2', 'AI_123')
droid_2 = Droid('R2D3', 'AI_456')

starship_1 = Starship('Space Cruiser')

starship_1.add_droids(droid_1)
starship_1.add_droids(droid_2)

starship_1.droids_communicate()
print(starship_1)