# 10. 
# Write a function that finds the largest even number in a list numbers. Return -1 if not found. You
# may not use the built-in functions max(), min(), sort(), or sorted().
    # Examples:
        # largest_even([3, 7, 2, 1, 7, 9, 10, 13]) → 10,
        # largest_even([1, 3, 5, 7]) → -1,
        # largest_even([0, 19, 18973623]) → 0

# Notes: my Logic:
# - Loop through each number
# - If it’s even → compare it to the previous largest even
# - If it’s larger → update the largest
# - If it’s odd → skip it
# - If no even numbers exist → return -1

def largest_even(fn_input):
    largest = -1

    for number in fn_input:
        if number % 2 == 0:
            if number > largest:
                largest = number
    
    result = largest
    return result
lyst_1 = [3, 7, 2, 1, 7, 9, 10, 13]
lyst_2 = [1, 3, 5, 7]
print(largest_even(lyst_1))
print(largest_even(lyst_2))