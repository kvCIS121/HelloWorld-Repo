def greeting(name, age = 'unk'):

    if age == 'unk':
        print(f'hello {name} how old are you?')
        
    else:
        print(f'hello {name}, it is cool being {age} yrs old')

greeting('timmy', 7)
greeting('dexter')


