a = int(input('Enter a number 1 - 3: '))
b = int(input('Enter a number 1 - 3: '))
c = int(input('Enter a number 1 - 3: '))

if a < b:
    winner = b
else:
    winner = a
if c > b:
    winner = c
print(f'The biggests number is: {winner}')