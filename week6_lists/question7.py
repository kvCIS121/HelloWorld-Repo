# 7. Write a function that takes 3 numbers as arguments, num_1 (first number), num_2 (second number),
# and num_3 (third number). Return a list of the integers in ascending order. 
# Do not use the built-in functions max(), min(), sort(), or sorted().
    # Examples:
        # ascending_order(2, 3, 1) → [1, 2, 3],
        # ascending_order(10, 1, 25) → [1, 10, 25],
        # ascending_order(2, 45, 4) → [2, 4, 45]

def ascending_order(num1, num2, num3):
    
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
        
    if num1 > smallest and num1 < largest:
        medium = num1
    elif num2 > smallest and num2 < largest:
        medium = num2
    else:
        medium = num3
    
    result = [smallest, medium, largest]        
    return result

number_range = [17, 1717, 777]
print(ascending_order(number_range[0], number_range[1], number_range[2]))