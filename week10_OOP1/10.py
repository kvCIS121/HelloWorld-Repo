# Create a Vector class.
# A Vector has
# ˆ x direction
# ˆ y direction

# A Vector can do
# ˆ get_magnitude

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.
# Hint: magnitude is calculated as sqrt(x**2 + y**2)

from math import sqrt
class Vector:
    # Constructor
    def __init__(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
        
    # Getters
    def get_x_direction(self):
        return self.x_direction
    def get_y_direction(self):
        return self.y_direction
    
    # Setters 
    def set_x_direction(self, new_x_direction):
        self.x_direction = new_x_direction
    def set_y_direction(self, new_y_direction):
        self.y_direction = new_y_direction

    # Methods
    def get_magnitude(self):
        return sqrt(self.x_direction **2 + self.y_direction **2)

vector1 = Vector(2,2)
print(vector1.get_magnitude())