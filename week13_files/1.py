import random

file = open('QuizInts.txt', 'w')

for numbers in range(100):
    number = random.randint(50,200)
    file.write(str(number) + '\n')

file.close()