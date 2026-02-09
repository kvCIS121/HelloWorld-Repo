height = int(input('enter a height: '))
pattern = input('enter a pattern: ')

for rows in range(1, height + 1):
    for columns in range(1 * rows, height + 1):
        print(pattern,end="")
    print()