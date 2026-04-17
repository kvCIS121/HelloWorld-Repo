import math 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
p1 = Point(3,4)
p2 = Point(0,0)

if p1 == p2:
    print('they are same')
else: 
    print('they are different')   

print('Distance', p1.distance(p2))

print('Point p1:', p1)