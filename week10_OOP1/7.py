# Create a Point class.
# A Point has
#  x coordinate
#  y coordinate

# A Point can do
#  print_info

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.
# Write a method called print_info, which prints in the form
# “(x,y)=([x coordinate], [y coordinate])”

class Point:
    # Constructor
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    # Getters
    def get_x_coordinate(self):
        return self.x_coordinate
    def get_y_coordinate(self):
        return self.y_coordinate
    
    # Setters
    def set_x_coordinate(self, new_x_coordinate):
        self.x_coorrdinate = new_x_coordinate
    def set_y_coordinate(self, new_y_coordinate):
        self.y_coordinate = new_y_coordinate
    
    # Method
    def print_info(self):
        print(f'(x,y) = ({self.x_coordinate},{self.y_coordinate})')
        
    
point1 = Point('x_coordinate', 'y_coordinate')
point2 = Point(7,7)
point3 = Point(4,4)
point1.print_info()
point2.print_info()
point3.print_info()