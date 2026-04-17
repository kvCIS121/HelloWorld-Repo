import random
number_file = open('numbers.txt', 'w')

for index in range(100):
    number = random.ranint(300,750)
    number_file.write(str(number))

# Note: str(3) = '3'