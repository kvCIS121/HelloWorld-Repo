# 13. 
# Write a function that takes two arguments, a list and an item. 
# The function should return the indices of all occurrences of the item in the list.
    # Examples:
        # get_indices( [1, 5, 5, 2, 7], 7) → [4]
        # get_indices( [1, 5, 5, 2, 7], 5) → [1, 2]
        # get_indices( [1, 5, 5, 2, 7], 8) → []
        # get_indices( [ ”a”, ”a”, ”b”, ”a”, ”b”, ”a”], ”a”) → [0, 1, 3, 5]

# for the 1st list, containing 5 integers, we're looking for the item, '7', which is 
# indext position 4. So, print out, and return the index position when '7' occurs

def get_indices(fn_input, item):
    result = []
        
    for i in range(len(fn_input)):
        if fn_input[i] == item:
            result.append(i)
    
    return result

tupple_1 = ( [1, 5, 5, 2, 7], 7)
tupple_2 = ( [1, 5, 5, 2, 7], 5)
tupple_3 = ( [1, 5, 5, 2, 7], 8)
tupple_4 = (['a', 'a', 'b', 'a', 'b', 'a'], 'a')

print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices( [1, 5, 5, 2, 7], 5))
print(get_indices([1, 5, 5, 2, 7], 8))
print(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'))