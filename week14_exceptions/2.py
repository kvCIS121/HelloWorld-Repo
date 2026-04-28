menu = ['apple', 'banana', 'cherry', 'date']

done = False
while not done:
    try:
        userInput = int(input('enter an index number to select a fruit: '))
        
        if userInput not in range(0, len(menu)):
            raise IndexError
        
        if userInput % 1 != 0:
            raise ValueError
        
    except IndexError:
        print('index out of range')

    except ValueError:
        print('invalid index format')
    
    else:
        result = menu[userInput]
        print(result)