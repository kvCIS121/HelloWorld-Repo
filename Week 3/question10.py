# Write a program that prompts the user to enter three integers and displays the integers in increasing
# order (smallest to largest). You may not use the built-in functions max (), min(), sort() or sorted 

small = 0
medium = 0
large = 0
x = int(input('enter a number: '))
y = int(input('enter a number: '))
z = int(input('enter a number: '))

    #finding smallest
if x <= y and x <= z:
    small = x
elif y <= x and y <= z:
    small = y
else:
    small = z
    #finding largest
if x >= y and x >= z:
    large = x
elif y >= x and y >= z:
    large = y
else: 
    large = z
    #finding middle
if x != small and x != large:
    medium = x
elif y != small and y != large:
    medium = y
else:
    medium = z

print(f'smallest, middle, to largest numbers are: {small}, {medium}, {large}')


