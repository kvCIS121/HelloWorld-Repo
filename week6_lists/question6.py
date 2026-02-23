# 6. 
# Write a function that returns a list with the factors of a given integer. The argument of the function
# will be num (integer to find factors for).
    # Examples:
        # find_factors(12) → [1, 2, 3, 4, 6, 12],
        # find_factors(17) → [1, 17],
        # find_factors(36) → [1, 2, 3, 4, 6, 9, 12, 18, 36]

def find_factors(fn_input):
    result = []

    for i in range(1, fn_input+1):
        if fn_input % i == 0:
            result.append(i)
    return result

n = int(input('enter a number: '))
print(find_factors(n))