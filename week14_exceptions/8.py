colorLyst = ['red', 'green', 'blue', 'yellow', 'purple']

done = False
while not done:

    try:
        userInput = int(input('enter an index value to print a color: '))

        if userInput not in range(0, len(colorLyst)):
            raise IndexError
        
        
    except IndexError:
        print('index out of range. try again')
    except ValueError:
        print('invalid input, try again')

    else:
        print(colorLyst[userInput])
        break # exits loop after a valid input

        