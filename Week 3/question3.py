light_color = input('Enter R, Y, or G for a traffic light: ')

if light_color == 'R' or light_color == 'r':
    print('STOP!')
elif light_color == 'Y' or light_color == 'y':
    print('YIELD!')
elif light_color == 'G' or light_color == 'g':
    print('GO!')
else:
    print('You did not follow directions for an input!')