# Create a Rectangle class.
# A Rectangle has
#  width
#  height

# A Rectangle can do
#  calculate area

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.
# The calculate_area() method should return the area calculated as: width * height.

class Rectangle:
    #constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    #getter
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    #setter
    def set_width(self, new_width):
        self.set_width = new_width
    def set_height(self, new_height):
        self.set_height = new_height
    
    #method
    def calculate_area(self):
        area = (self.width * self.height)
        return area

rectangle1 = Rectangle(4, 7)
rectangle1.calculate_area()
print(rectangle1.calculate_area())