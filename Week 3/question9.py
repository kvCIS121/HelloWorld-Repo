# This is the more efficient, advanced way to write the code using the help of MS CoPilot

user = input('Luke, enter the name of a family member: ')
relationship = {'Darth Vader':'Father', 'Leia':'Sister', 'Han':'Brother in law', 'R2D2':'Droid'}

if user in relationship:
    print(f' Luke, {user} is your {relationship[user]}!!!') 
else: 
    print(f'{user} is not your family, Luke!!!! STRANGER DANGER !!!!!!!')


# This was my way of coding, which is inefficient and more a beginners way

user = input('Luke, name a family member: ').lower()

f = 'Father'
s = 'Sister'
bil = 'Brother in law'
d = 'Droid'

if user == 'darth vader':
    print(f'Luke, {user} is your {f}')
elif user == 'leia':
    print(f'Luke, {user} is your {s}')
elif user == 'han':
    print(f'Luke, {user} is your {bil}')
elif user == 'r2d2':
    print(f'Luke, {user} is your {d}')
else:
    print(f'Luke, this is not your family !!!')

