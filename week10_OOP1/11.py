# Create a ColorRGB class.
# A ColorRGB has
#  red
#  green
#  blue

# A ColorRGB can do
#  to_grayscale

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.

# Instantiate an instance of the class. You may pass any initial values of your choosing.
# The to_grayscale() method should return the grayscale_value calculated as:
# 0.3 ∗ red + 0.59 ∗ green + 0.11 ∗ blue
# That is, it will just return a number (a float).

class ColorRGB:
    #constructor
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    #getters
    def get_red(self):
        return self.red
    def get_green(self):
        return self.green
    def get_blue(self):
        return self.blue
    
    #setters
    def set_red(self, new_red):
        self.red = new_red
    def set_green(self, new_green):
        self.green = new_green
    def set_blue(self, new_blue):
        self.blue = new_blue
    
    #methods
    def to_grayscale(self):
        grayscale_value = (0.3 * self.red + 0.59 * self.green + 0.11 * self.blue)
        return grayscale_value

color1 = ColorRGB(7,7,7)
color1.to_grayscale()
print(color1.to_grayscale())