try:
    number1 = int(input('enter first number: '))
    number2 = int(input('enter second number: '))
    
    difference = number1 - number2
    ratio = number1 / number2
    result = 0

    if number2 == 0:
        raise ZeroDivisionError
    else:
        result = f'Difference {int(difference)} , Ratio {float(ratio)}'
        print((result))

except OverflowError:
    print('result too large')

except ZeroDivisionError:
    print('cannot divide by zero')

except ValueError:
    print('invalid input')
    
    