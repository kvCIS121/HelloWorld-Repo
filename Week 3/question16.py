#scalene triangle = no sides are equal
#isosceles triangle = two sides are equal
#equilateral triangle = all sides are equal

done = False
while not done:
    side_1 = int(input('pick a side length: '))
    side_2 = int(input('pick a side length: '))
    side_3 = int(input('pick a side length: '))

    if side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
            triangle_type = ('Scalene Triangle')
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
       triangle_type = ('Isosceles Triangle')
    else:
        triangle_type = ('Equilateral Triangle')
    
    print(f'this is a {triangle_type}')