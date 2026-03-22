# 14. 
# Write a function named is_two_digit_number that returns a boolean value which determines if an
# integer is a two digit number. 
# 
# Write a second function named report two digit numbers that takes a
# list of integers and returns a new list containing all the two digit numbers from the original list. 
# 
# Call the is_two_digit_number function as part of the report two digit numbers function.
# Hint: a two digit number is one in the range [−99,−10] ∪ [10, 99].
    # Examples:
    #  report_two_digit numbers([100,57,12,1]) → [57,12]
    #  report_two_digit numbers([121,36,-19,-6,0,21]) → [36,-19,21]
    #  report_two_digit numbers([100,7,8437]) → []

def is_two_digit_number(n):
    if 10 <= n < 100:
        return True
    elif -100 < n <= -10:
        return True
    else:
        return False

def report_two_digit(lyst):
    result = []

    for numbers in lyst:
        if is_two_digit_number(numbers):
            result.append(numbers)
    return result

lyst = ([100,57,12,1])
print(report_two_digit(lyst))