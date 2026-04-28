done = False
while not done:
    try:
        userInput = float(input('enter a number: '))

        if userInput % 1 != 0:
            raise ValueError
        
        if userInput == 0:
            raise ZeroDivisionError
        result = userInput / 10
        print(f'{userInput} divided by 10 is {result}')
                      
    except ZeroDivisionError:
        print('you cannot divide by zero')
    except ValueError:
        print('please enter a valid number')

    else:
        print('great job! you followed the rules')
        done = True