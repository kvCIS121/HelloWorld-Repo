chickens = int(input("Enter # of chickens: "))
cows = int(input("Enter # of cows: "))
pigs = int(input("Enter # of pigs: "))

print(f'How many chickens do you have?: {chickens}')
print(f'How many cows do you have?: {cows}')
print(f'How many pigs do you have?: {pigs}')

total_legs = (2*chickens) + (4*cows) + (4*pigs)

print(f'The total amount of legs on your farm is {total_legs}')