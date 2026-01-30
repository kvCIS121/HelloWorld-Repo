small = 0
medium = 0
large = 0
x = int(input('enter a number: '))
y = int(input('enter a number: '))
z = int(input('enter a number: '))

    #finding the largest number
if x >= y and x >= z:
    large = x
elif y >= x and y >= z:
    large = y
else:
    large = z
    #finding smallest number
if x <= y and x <= z:
    small = x
elif y <= x and y <= z:
    small = y
else:
    small = z
    #finding medium/ middle number
if x != small and x != large:
    medium = x
elif y != small and y != large:
    medium = y
else:
    medium = z

print(f'large, medium, to smallest numbers are: {large}, {medium}, {small}')