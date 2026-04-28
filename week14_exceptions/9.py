destination = {'us':'united states', 'fr':'france', 'jp':'japan', 'br':'brazil'}

done = False
while not done:

    try:
        userInput = input('enter a country code, i.e., "us" for united states: ').lower() 
        # add .lower() to ensure capital or lower case letters both can be entered
        if userInput in destination:
            print(destination[userInput])
            break
        else:
            raise KeyError

    except KeyError:
        print('code not found, try again')