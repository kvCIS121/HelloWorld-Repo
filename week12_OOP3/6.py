class RGBColor: 
    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b
    
    def add(self, other):
        new_r = self.r + other.r
        new_g = self.g + other.g
        new_b = self.b + other.b

        if new_r > 255:
            new_r = 255
        if new_g > 255:
            new_g = 255
        if new_b > 255:
            new_b = 255

        third_equation = RGBColor((new_r/2), (new_g/2), (new_b/2))

        return third_equation
    
    def __str__(self):
        return f'RGBColor({self.r}, {self.g}, {self.b})'
    
c1 = RGBColor(170, 150, 200)
c2 = RGBColor(30, 100, 60)
c4 = RGBColor(700, 700, 700)
c5 = c1.add(c2).add(c4)
c3 = c1.add(c2) # I had to call c3 = c1+c2 as c1.add(c2) b/c add is a method
    

# Print readable color formats
print('c1: ', c1)
print('c2: ', c2)
print('c4: ', c4)
print('c1 + c2 + c4 = ', c5)
print('c3 = c1 + c2 => ', c3)