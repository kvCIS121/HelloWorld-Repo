# 3. Write a function that loops through and returns a list with every even number between two integers
# (inclusive). The arguments to the function will be smaller num and larger num.

# Examples:
# output_even(37, 1050) → [38, 40, 42, . . . 1048, 1050],
# output_even(1, 2000) → [2, 4, 6, . . . 1998, 2000],
# output_even(50, 199) → [50, 52, 54, . . . 196, 198]

def output_even(smaller_num, larger_num):
    result = []

    for i in range(smaller_num, larger_num):
        if i % 2 == 0:
            result.append(i)
    return result

fn_input = [37, 1050+1]
print(output_even(fn_input[0], fn_input[1]))

# LINE 17 * LINE 18 is a list, index position 0 = 37;  index position 1 = 1050+1; 
# so
# number_range[0] = 37, and number_range[1] = 1051, 
# feeds back up to where x and y in range(x,y), because the function is OUTPUT_EVEN(X, Y)
# and we called it thru line 17 by printing: print(output_even(number_range[0], number_range[1]))
# The MOST IMPORTANT part is line 17 and line 18, calling the function w/ correct list index position and integer value into
# the function