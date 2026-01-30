import math

pi = math.pi
r = int(input('Enter the radius: '))
volume_sphere = (4/3) * pi * (r**3)

print(f'The volume of a sphere is V = {round(volume_sphere, 1)}')