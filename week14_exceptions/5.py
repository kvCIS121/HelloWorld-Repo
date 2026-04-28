studentScores = {'alice':90, 'bob':75, 'charlie':60}

studentName = input('enter student name: ')# <-- we can add .lower() to ensure Alice, ALICE, aLICe, etc are all included
numberToAdd = int(input('enter a number to add: '))


try:
    if studentName in studentScores:
        result = numberToAdd + studentScores[studentName]
        print(result)
    else:
        raise KeyError
        raise ValueError
except KeyError:
    print('student not found')
except ValueError:
    print('invalid number')