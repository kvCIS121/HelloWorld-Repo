import math


pi = math.pi


radius = 5
example = 5 ** 2 #double multiplication is squaring the integer => (5^2)
r = radius

# Formula is Pi R^2
area_of_circle = pi * r**2
print(area_of_circle)

# Formula for sphere => (4/3) pi r^3
volume_of_sphere = (4/3) * pi * r**3
print(f"If the radius is  = {r} the area must be {round(area_of_circle, 1)} and the volume is {round(volume_of_sphere, 1)}")

# How to round a value or integer to one, two, three, etc decimal place values
# Ex. {round(area_of_circle, 1)} <= the comma, and then '1' means to round the area_of_circle to 1 decimal place 

import math #- The math module provides common mathematical functions and constants like square root, trigonometry, logarithms, and more.


sum = 5 + 10
print(sum)

product = 5 * 2
print(product)

subtraction = sum - product
print(subtraction)

divide = sum / 2
print(divide)

modulus = divide % 2
print(modulus)

# Floor Division (used to exclude decimal values and only print out the nearest whole number for division of two integers)
floorDiv = 10 // 3
print(floorDiv)

#type casting to a different data type
floorDiv2 = int(10 / 3)
print(floorDiv2)

pie = math.pi # I was able to pull this using the IMPORT MATH library above
print(pie)

# Floor Division is using double back-slash to divide two integers and print the result to the neares WHOLE number only,
# it will leave out/ exclude the decimal value...
floorDiv2 = int(10 / 3)
print(floorDiv2)

# "%" = the Modulus arithmetic operator: means to divide and print the remainder
modulus = 271 % 3
print(modulus)

# BOOLEAN OPERATORS
# " + " : addition
# " - " : subtraction
# " / " : division
# " * " : multiplication
# " == " : means, "is equal to" -> ex1: 3 == 3 (three is equal to three) ex2: 3 == 4 (3 is equal to 4) NOT TRUE!
    #: ex. When using == or = in "if statement, the y = 3 and [if y = 4]<- this is not saying y != 3. It changes the variable y to 4!!!"
# " != " : means, NOT EQUAL TO
# " < " : means, less than
# " > " : means, more than
# " <= ": means, less than or equal to
# " >= ": means, more than or equal to
# " or ": can have 2 meanings. One, it can mean (inclusive). Two, it can mean (exclusive) Therefore, we change spelling.
    #         exclusive will be respelled as XOR
    #         We just need to know that for OR, it means: one or the other or both are true
# " += ": means, add & assign. Basically, add the value on the right to the old variable, and assign it as a new value for the current variable
# " -= ": means, subtract & assign
# " * = ": means, multiply and assign
# " /= ": means, divide and assign
# " // "
# "not a": one is true, the other is not true
# " % " : Modulus Operator - Divides two integers, and returns the REMAINDER
    # ex. 
    #   using 7 as dividend, 3 as divisor: if 7 divide by 3 = 2 remainder 1
    #   then, 7 % 3 = 1 (because it returns the remainder as the value for Modulus operator)     

x = 3
y = 4
print(x == y) # x != y, therefore, it will print "False"

# SELECTION STATEMENTS
# if
# if-else
# if <condition>:
#       <block of code> if it is true, perform this code

    # Ex1: Note, block of code is indicated by a tab out from the condition. We cannot interchange/ use tabs and spaces. Code will fail
