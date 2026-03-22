def pool_times(grades, times):
  
    while True:

        if grade in range(0, 3+1):
            if time == 'morning':
                return '9am'
            else:
                return '1pm'
        elif grade in range(4, 8+1):
            if time == 'morning':
                return '10am'
            else:
                return '2pm'
        elif grade in range(9, 12+1):
            if time == 'morning':
                return '11am'
            else:
                return '3pm'
            
grade = int(input('enter a grade (enter 0 for kindergarten): '))
time = input('morning or afternoon: ')
                
print(pool_times(grade, time))