height = int(input('enter a number: '))
pattern = input('enter a pattern: ')
rows = 0
columns = 0

for rows in range(1, height + 1):
    for columns in range(1, rows + 1):
        print(pattern, end="")
    print()