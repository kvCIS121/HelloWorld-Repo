lyst = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

try:
    userInput = int(input('enter a number, 0-6; ea/ corresponds to a day: 0 for Monday, 6 for Sunday: '))
    if userInput in range(0, len(lyst)):
        print(lyst[userInput])
    else:
        raise ValueError
        
except ValueError:
    print('invalid input')
    