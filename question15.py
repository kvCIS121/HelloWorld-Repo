# 15. 
# Write a function named is_negative that returns a boolean value which determines if an integer is
# a negative number. 
# 
# Write a second function named is_odd that returns a boolean value which determines
# if an integer is odd. 
# 
# Write a third function named report_negative_oddds that takes a list of
# integers and returns a new list containing all the negative odd numbers from the original list. 
# 
# The report_negative_oddds function must call the is_negative and is_odd to determine if an element belongs.
    # Examples:
    #  report_negative_oddds([100,-57,12,1,-36,-15]) → [-57,-15]
    #  report_negative_oddds([121,-101,36,-19,-6,0,21,-1]) → [-101,-19,-1]
    #  report_negative_oddds([-100,7,8437]) → []

def is_negative(n):
    if n < 0:
        return True
    else:
        return False

def is_odd(n):
    if -n % 2 == 1:
        return True
    else:
        return False

def report_negative_odds(lyst):
    result = []

    for numbers in lyst:
        if is_negative(numbers):
            if is_odd(numbers):
                result.append(numbers)
    return result

lyst_1 = ([100,-57,12,1,-36,-15])
lyst_2 = ([121,-101,36,-19,-6,0,21,-1])
lyst_3 = ([-100,7,8437])

print(report_negative_odds(lyst_1))
print(report_negative_odds(lyst_2))
print(report_negative_odds(lyst_3))