catalog = {'apple':1.5, 'banana':0.9, 'cherry':2.2}

done = False
while not done:
    try:
        userInput = input('enter a product name: ')
    
        if userInput not in catalog:
            raise KeyError
        else:
            print(catalog[userInput])
            
    except KeyError:
        print('Product not found')