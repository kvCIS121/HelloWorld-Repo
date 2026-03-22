# a Mutable object is changeable, an Immutable object cannot be changed

#   EXAMPLE 1:

lyst_1 = [1,2,3]
lyst_2 = lyst_1

lyst_2.append(4)

print(lyst_1)

#   EXAMPLE 2: NOT MUTABLE

x = 'hi'
y = '!'
z = x+y
print(z)

