# 11. Write a function that finds the largest odd number in a list numbers. Return -1 if not found. 
# You may not use the built-in functions max(), min(), sort(), or sorted().
#   Examples:
    # largest_odd([3, 7, 2, 1, 7, 9, 10, 13]) → 13,
    # largest_odd([2, 4, 6, 8]) → -1,
    # largest_odd([0, 19, 18973623]) → 18973623

def largest_odd(fn_input):
    largest = -1

    for number in fn_input:
        if number % 2 == 1:
            if number > largest:
                largest = number
    result = largest
    return result
lyst_1 = [3, 7, 2, 1, 7, 9, 10, 13]
lyst_2 = [2, 4, 6, 8]
print(largest_odd(lyst_1))
print(largest_odd(lyst_2))