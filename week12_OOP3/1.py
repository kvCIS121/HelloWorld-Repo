import math

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other_vector):
        return self.a == other_vector.a and self.b == other_vector.b
        
    def __add__(self, other_vector):
        new_a = self.a + other_vector.a
        new_b = self.b + other_vector.b
        return Vector(new_a, new_b)

    def __str__(self):
        # v = ax + by
        return f'({self.a}x + {self.b}y)'


v1 = Vector(6,7)
v2 = Vector(6,7)
v3 = Vector(1,2)
v4 = Vector(3,4)

# Print readable versions
print('vector1: ', v1)
print('vector2: ', v2)
print('vector3: ', v3)
print('vector4: ', v4)

if v1 == v2:
    print('they are same')
else:
    print('they are different')

if v3 == v4:
    print('they are same')
else:
    print('they are different')


# Add three vectors together
v_sum = v1 + v3 + v4
print("Sum of vectors:", v_sum)