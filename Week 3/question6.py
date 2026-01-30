coinFlip = int(input('Guess whether the flip of a coin is 1 or 0: ')) 

from random import randint #this is the import for picking a random number
value = randint(0,1) #sets 'value' = to the import 'randint', picks a random integer, either 0 or 1

print(f'The random selected number is {value}, therefore: ')

if value == coinFlip:
    print(f'You picked {coinFlip}, you win!')
else:
    print(f'You picked {coinFlip}, you lose!')
if value != coinFlip:
        print(f'You picked a that is not 1 or 0!!!!!!')





    