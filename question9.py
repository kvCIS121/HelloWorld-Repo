# 9. Write a function that takes two arguments, a list and a value. The function should return the indices
# of all occurrences of the value in the list, if no argument is provided then the default should be to
# find 0.

# Examples:
# get_indices( [1, 0, 5, 0, 7] ) → [1, 3]
# get_indices( [1, 5, 5, 2, 7], 7) → [4]
# get_indices( [1, 5, 5, 2, 7] ) → [ ]
# get_indices( [1, 5, 5, 2, 7], 5) → [1, 2]
# get_indices( [1, 5, 5, 2, 7], 8) → [ ]
# get_indices( [ ”a”, ”a”, ”b”, ”a”, ”b”, ”a”], ”a”) → [0, 1, 3, 5]

def get_indices(lyst, value = 0):
    result = []

    for number in range(len(lyst)):
        if lyst[number] == value:
            result.append(number)
    return result

lyst_1 = ( [1, 0, 5, 0, 7], )
lyst_2 = ( [1, 5, 5, 2, 7], 7)
lyst_3 = ( [1, 5, 5, 2, 7], )
lyst_4 = ( [1, 5, 5, 2, 7], 5)
lyst_5 = ( [1, 5, 5, 2, 7], 8)
lyst_6 = ( [ 'a', 'a', 'b', 'a', 'b', 'a'], 'a')

print(get_indices(lyst_1[0], ))
print(get_indices(lyst_2[0], lyst_2[1]))
print(get_indices(lyst_3[0], ))
print(get_indices(lyst_4[0], lyst_4[1]))
print(get_indices(lyst_5[0], lyst_5[1]))
print(get_indices(lyst_6[0], lyst_6[1]))
