class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return  self.width * self.height
        
    def __mul__(self, other):
        new_width = self.width * other
        new_height = self.height * other
        return Rectangle(new_width, new_height)
    
    def __str__(self):
        return f'Rectangle({self.width} x {self.height})'

# Rectangle objects    
rectangle_1 = Rectangle(4,5)
rectangle_2 = Rectangle(3,2)


# Readable format of rectangle objects
print(rectangle_1)
print(rectangle_2)

# Execute program instructions, multiplying rectangles 1 & 2 by an integer 
rectangle_3 = rectangle_1 * 3
rectangle_4 = rectangle_2 * 3

print(rectangle_3)
print(rectangle_4)

# Use the area() method to find the areas of rectangle's 1 and 2
print('area of rectangle_1 = ', rectangle_1.area())
print('area of rectangle_2 = ', rectangle_2.area())