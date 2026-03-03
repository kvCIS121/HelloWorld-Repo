# 8. In each input list, every number repeats at least once, except for two. 
# Write a function that takes an array numbers and returns the two unique numbers.
    # Examples:
        # return_unique([1, 9, 8, 8, 7, 6, 1, 6]) → [9, 7],
        # return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) → [2, 1],
        # return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) → [5, 6]

def return_unique(numbers):
    unique_numbers = {}
   
    for n in numbers:
        if n in unique_numbers:
            unique_numbers[n] += 1
        else:
            unique_numbers[n] = 1
            
            result = []
    for n in unique_numbers:
        if unique_numbers[n] == 1:
            result.append(n)
    return result    
            
lyst_1 = ([1, 9, 8, 8, 7, 6, 1, 6])
lyst_2 = ([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
lyst_3 = ([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])

print(return_unique(lyst_1))
print(return_unique(lyst_2))
print(return_unique(lyst_3))