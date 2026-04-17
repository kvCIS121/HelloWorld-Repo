class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return RationalNumber(new_numerator, new_denominator)
    
    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

# Create object
r1 = RationalNumber(3,5)
r2 = RationalNumber(2,6)

r3 = r1.add(r2)


print('r1: ', r1)
print('r2: ', r2)
print('r3: ', r3) 
