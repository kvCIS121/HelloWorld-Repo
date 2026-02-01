done = False

while not done:
    grade = int(input('enter your grade. note: if in kindergarten, k, then enter "0": '))
    k = 0

    if grade in range(13, 99+1):    #set the grade >=13 here because it tests right away if older, than the next prompts aren't necessary
        print(f'you are too old, please go somewhere else!')    #need to insert CONTINUE here so that code doesn't proceed to ask "swim_options" and will reset from top question
        continue

    swim_options = input("enter 'morning' OR 'afternoon': ")
    
    if grade in range(0, 3+1) and swim_options == 'morning':
        pool_opens = '9 am'
    elif grade in range(0, 3+1) and swim_options == 'afternoon':
        pool_opens = '1 pm'
    elif grade in range(4, 8+1) and swim_options == 'morning':
        pool_opens = '10 am'
    elif grade in range(4, 8+1) and swim_options == 'afternoon':
        pool_opens = '2 pm'
    elif grade in range(9, 12+1) and swim_options == 'morning':
        pool_opens = '11 am'
    elif grade in range(9, 12+1) and swim_options == 'afternoon':
        pool_opens = '3 pm'
    else:
        print(f'the pool is CLOSED at this time. choose a valid option')
        continue
    
    
    print(f'the pool is open at {pool_opens}')