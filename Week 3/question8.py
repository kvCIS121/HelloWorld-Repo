# version 1 ----

ice_cream = input('Which flavor ice cream do you want?: ')
flavors = ('vanilla, strawberry, chocolate')

if ice_cream in flavors:
    print(f'Here is your {ice_cream} ice cream!')
else:
    print('Sorry, we do not have that flavor')

# version 2 ----

ice_cream = input('Which flavor ice cream do you want?: ')
flavors = ('vanilla, strawberry, chocolate')

if ice_cream == 'vanilla' or ice_cream == 'strawberry' or ice_cream == 'chocolate':
    print(f'Here is your {ice_cream} ice cream!')
else:
    print('Sorry, we do not have that flavor')