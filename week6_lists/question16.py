# 16. 
# There’s a great war between the even and odd numbers. Many numbers already lost their lives in this
# war and it’s your task to end this. You have to determine which group sums larger: the evens or the
# odds. The larger group wins.

# Write a function that takes a list of integers named numbers, sums the even numbers and odd numbers
# separately, then returns which of the two sums is larger.
    
    #  Examples:
        # war_of_numbers([2, 8, 7, 5]) → ”odds”, (since 2 + 8 = 10, 7 + 5 = 12, odds is larger)
        # war_of_numberss([12, 90, 75, 1, 1]) → ”evens”, (12 + 90 = 102, 75 + 1 + 1 = 77, evens is larger)
        # war_of_numbers([2, 10, 22, 243]) → ”odds”

def war_of_numbers(integers):
    sum_even = 0
    sum_odd = 0

    for numbers in integers:
        if numbers % 2 == 0:
            sum_even = sum_even + numbers
        elif numbers % 2 == 1:
            sum_odd = sum_odd + numbers
        if sum_even > sum_odd:
            sum = 'evens are larger'
        else:
            sum = 'odds are larger'
    sum = sum
    return sum

numbers_list_1 = [2, 8, 7, 5]
numbers_list_2 = [12, 90, 75, 1, 1]
numbers_list_3 = [2, 10, 22, 243]

print(war_of_numbers(numbers_list_1))
print(war_of_numbers(numbers_list_2))
print(war_of_numbers(numbers_list_3))