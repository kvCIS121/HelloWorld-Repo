done = False
while not done:
    try:
        prizeAmount = int(input('enter prize amount: '))
        numberOfWinners = int(input('enter number of winners: '))

        if numberOfWinners == 0:
            raise ZeroDivisionError
        else:
            reward = (prizeAmount / numberOfWinners)
            print(reward)
            break

    except ValueError:
        print('invalid input, try again')
    except ZeroDivisionError:
        print('cannot divide by zero')