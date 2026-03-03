# 10. Below is the menu from my favorite restaurant.
# 
# (a) Initialize an empty dictionary named menu, and then add the contents of the menu as key-value
# pairs.
# (b) Using the dictionary you created in part a, write code that prints each of the items on the menu
# as key-value pairs. 
# 
# The code should work regardless of the contents of the receipt. (meaning don’t
# write print( ”burger”, 10))
    # Item Price
        # burger $10
        # fries $4
        # soda $3

menu={}
menu['burger']=10
menu['fries']=4
menu['soda']=3

#   1st Option of writing a program to print key-value pairs for Menu dictionary
for keys in menu.keys():
    values = menu[keys]
    print(keys, values)

#   2nd Option, which is shorter and more 'simple'
for keys, values in menu.items():
    print(keys, values)