import math

r = int(input('Enter the radius: '))
h = int(input('Enter the height: '))
pi = math.pi
volume_cylinder = (pi)*(r**2)*(h)

print(f'The volume of a cylinder is V = {round(volume_cylinder, 1)}')