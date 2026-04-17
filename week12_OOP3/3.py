class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    
    def __str__(self):
        if self.b >= 0:
            # z = a + bi
            return f'({self.a} + {self.b}i)'
        else:
            return f'({self.a} - {abs(self.b)}i)'

# Instantiate two ComplexNumbers
z1 = ComplexNumber(1,2)
z2 = ComplexNumber(3,4)

# Print readable versions
print("First number:", z1)
print("Second number:", z2)

# Compare them
if z1 == z2:
    print('They are the same')
else:
    print('They are different')