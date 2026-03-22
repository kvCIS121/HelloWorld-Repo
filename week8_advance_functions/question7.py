# 7. 
# Write a function that takes 3 numbers as arguments, num 1 (first number), num 2 (second number),
# and num 3 (third number). num 1 should be mandatory. If no arguments are provided for num 2 or
# num 3 then use 5 for num 2 and 25 for num 3. 

# Return a list of the integers in ascending order.
# You may not use the built-in functions max(), min(), sort(), or sorted().\

# Examples:
# ascending_order(2, 3, 1) → [1, 2, 3],
# ascending_order(10, 1) → [1, 10, 25],
# ascending_order(50) → [5, 25, 50]

def ascending_order(num1, num2=5, num3=25):
    result = []

    if num1 < num2 and num1 < num3:
        smallest = num1
    elif num2 < num1 and num2 < num3:
        smallest = num2
    else:
        smallest = num3
        
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    else:
        largest = num3
    
    if smallest < num1 and num1 < largest:
        medium = num1
    elif smallest < num2 and num2 < largest:
        medium = num2
    else:
        medium = num3
 
    result = [smallest, medium, largest]
    return result

lyst_1 = (2,3,1)
lyst_2 = (10,1)
lyst_3 = (5,25,50)

print(ascending_order(lyst_1[0], lyst_1[1], lyst_1[2]))
print(ascending_order(lyst_2[0], lyst_2[1]))
print(ascending_order(lyst_3[0], lyst_3[1], lyst_3[2]))