# 12. Write a function named is_even that returns a boolean value which determines if an integer is even.
# Write a second function named report_evens that takes a list of integers and returns a new list containing
# all the even numbers from the original list. Call the is_even function as part of the report_evens function.
    
    # report_evens([4,3,12,16,8,9,25]) → [4,12,16,8]
    # report_evens([6,100,3,12,16,6,9,100]) → [6,100,12,16,6,100]
    # report_evens([3,99,7,13,25]) → []

def is_even(num):

    result = []

    for n in num:
        if n % 2 == 0:
            result.append(n)
    return result
      
report_evens_1 = ([4,3,12,16,8,9,25])
report_evens_2 = ([6,100,3,12,16,6,9,100])
report_evens_3 = ([3,99,7,13,25])

print(is_even(report_evens_1))
print(is_even(report_evens_2))
print(is_even(report_evens_3))