import math

pi = math.pi
r = int(input('Enter the radius: '))
h = int(input('Enter the height: '))
volume_cone = (pi) * ((r**2) * h) / 3

print(f'The volume of a cone is V = {round(volume_cone, 1)}')