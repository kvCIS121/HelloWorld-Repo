# 2. (Game: Odd or Even) Write a function that lets the user guess whether a randomly generated number
# is odd or even. The function randomly generates an integer between 0 and 9 (inclusive) and returns
# whether the user’s guess is correct or incorrect. The argument for the function will be guess (the user’s
# guess, either ”odd” or ”even”), if no argument is provided then the default guess should be even.
# Hint: Use the following lines of code to create the function.
# 
# from random import randint
# value = randint(0,9) #picks a random integer between 0-9 inclusive
# 
# Examples:
#   guess( ) → ”Correct!” (if random value is even) or ”Incorrect!” (if random value is odd)
#   guess( ”odd”)→ ”Correct!” (if random value is odd) or ”Incorrect!” (if random value is even)
#   guess( ”even”) → ”Correct!” (if random value is even) or ”Incorrect!” (if random value is odd)

from random import randint

def even_or_odd(guess = 'even'):

    value = randint(0, 9)
    
    if user_guess == 'even':
        if value % 2 == 0:
            return 'Correct!'
        else:
            return 'Incorrect!'
    elif user_guess == 'odd':
        if value % 2 == 1:
            return 'Correct!'
        else:
            return 'Incorrect!'

user_guess = input('enter "odd" or "even": ')
print(even_or_odd(user_guess))