# 8. 
# Write a function that takes 3 numbers as arguments, num 1 (first number), num 2 (second number),
# and num 3 (third number). Return a list of the integers in descending order. 

#You may not use the built-in functions max(), min(), sort(), or sorted().
    # Examples:
        # descending_order(2, 3, 1) → [3, 2, 1],
        # descending_order(10, 1, 25) → [25, 10, 1],
        # descending_order(2, 45, 4) → [45, 4, 2]

def descending_order(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    else:
        largest = num3
    
    if num1 < num2 and num1 < num3:
        smallest = num1
    elif num2 < num1 and num2 < num3:
        smallest = num2
    else:
        smallest = num3
    
    if smallest < num1 and num1 < largest:
        medium = num1
    elif smallest < num2 and num2 < largest:
        medium = num2
    else:
        medium = num3

    results = [largest, medium, smallest]
    return results

number_lyst = [717, 777, 7]
print(descending_order(number_lyst[0], number_lyst[1], number_lyst[2]))