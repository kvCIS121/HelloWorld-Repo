# 4. Write a function that loops through and returns a list with every odd number between two integers
# (inclusive). The arguments to the function will be smaller num and larger num.

# Examples:
# output_odd(37, 1050) → [37, 39, 41, . . . , 1049],
# output_odd(1, 2000) → [1, 3, 5, . . . , 1999],
# output_odd(50, 199) → [51, 53, 55, . . . , 197, 199]

def output_odd(smaller_num, larger_num):
    result = []

    for i in range(smaller_num, larger_num):
        if i % 2 == 1:
            result.append(i)
    return result

number_range = [37, 1050+1]
print(output_odd(number_range[0], number_range[1]))