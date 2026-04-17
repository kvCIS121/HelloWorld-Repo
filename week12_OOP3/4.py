class LinearEquation:
    def __init__(self,m,b):
        self.m = m
        self.b = b
    
    def __add__(self,other):
        new_m = self.m + other.m
        new_b = self.b + other.b
        
        return LinearEquation(new_m, new_b)
    
    def __str__(self):
        # y = mx + b
        return f'y = {self.m}x + {self.b}'

y1 = LinearEquation(2,3)
y2 = LinearEquation(-1,5)

print(y1)
print(y2)

y_sum = y1 + y2
print(y_sum)