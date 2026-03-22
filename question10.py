# 10. Write a function that returns the factors of a given integer. The argument of the function will be
# 'num' (integer to find factors for), if no argument is provided then the default should be 36.

# Examples:
# find_factors(12) → 1, 2, 3, 4, 6, 12
# find_factors(17) → 1, 17,
# find_factors(36) → 1, 2, 3, 4, 6, 9, 12, 18, 36
# find_factors( ) → 1, 2, 3, 4, 6, 9, 12, 18, 36

def find_factors(num = 36):
    result = []

    for number in range(1, num + 1):
        if num % number == 0:
            result.append(number)

    return result
num_1 = 12
num_2 = 17
num_3 = 36

print(find_factors(num_1))
print(find_factors(num_2))
print(find_factors(num_3))
print(find_factors())