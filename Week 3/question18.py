done = False
while not done:
    race = input('what race are you. "elf" or "ogre": ')
    
    class_status = input('what class are you. "warrior", "bard", or "wizard": ')
    
    health_points = 0

    if race == 'elf' and class_status == 'warrior':
        health_points = 150
    
    elif race == 'ogre' and class_status == 'warrior':
        health_points = 200
    
    elif race == 'elf' and class_status == 'bard':
        health_points = 75
    
    elif race == 'ogre' and class_status == 'bard':
        health_points = 100
    
    elif race == 'elf' and class_status == 'wizard':
        health_points = 25
    
    elif race == 'ogre' and class_status == 'wizard':
        health_points = 50

    else: 
        print(f'invalid search. try again')
        continue
        #continue means: “Skip everything below this point and jump back to the top of the loop.”
        #this prevents the last print line from executing, which is not necessary since the search is invalid
    
    print(f'an {race} is a {class_status} with {health_points} health points')