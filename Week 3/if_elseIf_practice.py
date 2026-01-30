budget = float(input('put ur budget: '))
price = 0
num_units = 0
max_units = 0 # the max units we can buy with our budget 

while num_units <= 1000:
    if num_units <= 100:
        price = 3.99
    elif num_units <= 300:
        price = 2.99
    else:
        price = 1.99

    if (price * num_units) <= budget and num_units > max_units:
        max_units = num_units
    
    print(f'The price for {num_units} units is ${price * num_units}')
    num_units = num_units + 1