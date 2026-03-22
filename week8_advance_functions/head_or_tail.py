coinFlip = int(input('Guess whether the flip of a coin is 1 or 0: ')) 

from random import randint #this is the import for picking a random number
value = randint(0,1) #sets 'value' = to the import 'randint', picks a random integer, either 0 or 1

print(f'The random selected number is {value}, and since: ')

if value != '0' or value != '1':
        print(f'You picked a number that is not 1 or 0, TRY AGAIN!')
elif value == coinFlip:
    print(f'You picked {coinFlip}, you win!')
else:
    print(f'You picked {coinFlip}, you lose!')

#+++++
#very simple version:

from random import randint
value = randint(0,1)
coin_flip = int(input('pick "0" or "1": '))

if value == coin_flip:
    print('you win!')
else:
    print('you lose!')


    