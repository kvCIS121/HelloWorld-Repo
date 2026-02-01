done = False

while not done:
    age = int(input('enter your age: '))
    athleticism_goal = input('enter your athleticism goal, either "below average" or "above average": ')
    resting_heart_rate = 0

    if age in range(20, 39+1) and athleticism_goal == 'below average':
        resting_heart_rate = ('73 - 93')
    elif age in range(20, 39+1) and athleticism_goal == 'above average':
        resting_heart_rate = ('47 - 72')
    
    
    
    if age in range(40, 59+1) and athleticism_goal == 'below average':
        resting_heart_rate = ('72 - 94')
    elif age in range(40, 59+1) and athleticism_goal == 'above average':
        resting_heart_rate = ('46 - 72')
   
     
    
    if age in range(60, 79+1) and athleticism_goal == 'below average':
        resting_heart_rate = ('71 - 97')
    elif age in range(60, 79+1) and athleticism_goal == 'above average':
        resting_heart_rate = ('45 - 70')
   
  
    print(f'your resting hear rate should be between {resting_heart_rate}')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

done = False

while not done:
    age = int(input('enter your age: '))
    athleticism_goal = input('enter your athleticism goal, either "below average" or "above average": ')
    resting_heart_rate = 0

    if age >= 20 and age <= 39:
        if athleticism_goal == 'above average':
            resting_heart_rate = '47 - 72'
        else:
            resting_heart_rate = '73 - 93'

    if age >= 40 and age <= 59:
        if athleticism_goal == ' above average':
            resting_heart_rate = '46 - 71'
        else:
            resting_heart_rate = '72 - 94'
    
    if age >= 60 and age <= 79:
        if athleticism_goal == 'above average':
            resting_heart_rate = '45 - 70'
        else:
            resting_heart_rate = '71 - 97'
    
    print(f'your resting heart rate should be between {resting_heart_rate}')


#Notes about Nesting, which is like example 2

#Another way of writing this code using nesting
#Nesting means putting one control structure inside another:
#Example of nesting: 
        #   if condition1:          if x < y and x < z: (x could be less than y, but it may not be less than z vise versa)
        #       if condition2:          if y < z: (if y is less than z, then in fact x is the smallest)
        #           do_something            print(f'the smallest integer is {x}')
