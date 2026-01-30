a = int(input('Enter any number: '))
b = int(input('Enter any number: '))
c = int(input('Enter any number: '))

if a < b:
    winner = a
else:
    winner = b
if c > winner:
    winner = winner
else:
    winner = c
print(f'The winner is {winner}') 