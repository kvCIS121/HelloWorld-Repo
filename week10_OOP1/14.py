# Create a Circle class.
# A Circle has
#  radius

# A Circle can do
#  calculate circumference

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.
# The calculate circumference() method should return the circumference calculated as: 2 · π · radius.

from math import pi
print(f'PI = {pi}')

class Circle:
    #constructor
    def __init__(self, radius):
        self.radius = radius
    
    #getter
    def get_radius(self):
        return self.radius
    
    #setter
    def set_radius(self, new_radius):
        self.radius = new_radius
    
    #method
    def calculate_circumference(self):
        circumference = (2 * pi * self.radius)
        return circumference

circle1 = Circle(7)
circle1.calculate_circumference()
print(circle1.calculate_circumference())
