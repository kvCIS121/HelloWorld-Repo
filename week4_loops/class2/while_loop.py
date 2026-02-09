user_number = int(input('enter a number: '))

while user_number >= 1: #using 1 as the comparison stops the integer from further dividing by decimal values, which will be infinity
    user_number = user_number / 2
    print(user_number)