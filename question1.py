# 1. (Game: heads or tails) Write a function that lets the user guess whether the flip of a coin results in
# heads or tails. The function randomly generates an integer 0 or 1, which represents head or tail. The
# function returns if the guess is correct or incorrect. The argument for the function will be guess (the
# guess of the user, 0 for heads and 1 for tails), if no argument is provided then the default should be
# 0 for heads.
    # Hint: Use the following lines of code to create the function.
#   from random import randint
#   value = randint(0,1) #picks a random integer. Either 0 or 1.
        # Examples:
            # toss_coin( ) → ”Correct!” (if the random value is 0) or ”Incorrect!” (if the random value is 1),
            # toss_coin(0) → ”Correct!” (if the random value is 0) or ”Incorrect!” (if the random value is 1),
            # toss_coin(1) → ”Correct!” (if the random value is 1) or ”Incorrect!” (if the random value is 0)

from random import randint

def toss_coin(guess = 0):
    value = randint(0,1)

    if guess == value:
        return 'Correct!'
    else:
        return 'Incorrect!'

user_guess = int(input('enter 0 or 1: '))
print(toss_coin(user_guess))
