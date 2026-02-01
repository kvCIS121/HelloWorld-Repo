done = False

while not done:
    check_for_highway = int(input('enter a number: '))

    
    if check_for_highway in range(100, 1000, 1):    #starts at 100, stops at 9999, increments by 1 -> 100, 101, 102, etc.
        if check_for_highway in range(100, 1000, 100): #starts at 100, stops at 999, increments by 100's. i.e. 100, 200, 300 etc
            print(f'{check_for_highway} is an invalid Auxillary highway, try again')
        else:
            print(f'Auxillary Highway {check_for_highway} services primary highways')
    
    elif check_for_highway in range(2, 100, 2): #starts in range at 2, stops at 99, increments by 2, checking for even numbers
        print(f'Interstate Highway {check_for_highway} runs East/West') 

    elif check_for_highway in range(1, 100, 2): #starts at 1, stops at 99, increments by 1, checking for odd numbers
        print(f'Interstate Highway {check_for_highway} runs North/South')

    else:   #if not even or odd numbers between this range or in the 100's range, then print invalid highway
        print(f'{check_for_highway} is an invalid highway number')
    
           