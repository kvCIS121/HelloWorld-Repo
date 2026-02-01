x = int(input('pick a number: '))
y = int(input('pick a number: '))
z = int(input('pick a number: '))

if x == y or x == z:
    if y == z:
        print('all 3 integers are equal')
    else:
        print('only 2 integers are equal')
elif y == z:
    print('only 2 integers are equal')
else:
    print('all 3 integers are unique')