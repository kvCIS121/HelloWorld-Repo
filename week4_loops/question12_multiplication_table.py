#   Printing a Multiplication Table
#   uses nested loops

x_axis = int(input('enter a number: '))
y_axis = int(input('enter a number: '))
numbers = 0

for rows in range(1, x_axis + 1):
    for columns in range(1, y_axis + 1):
        print(rows * columns, end = " ")
    print()