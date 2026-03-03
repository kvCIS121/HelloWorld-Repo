# 7. In each input list, every number repeats at least once, except for one. 
# Write a function that takes an
# array numbers and returns the single unique number.
    # Examples:
        # find_unique([1, 2, 2, 3, 3, 4, 4]) → 1,
        # find_unique([7, 8, 8, 9, 9, 10, 10]) → 7,
        # find_unique([5, 6, 6, 7, 7, 8, 8, 5, 9]) → 9

def find_unique(numbers):
    unique_number = {}

    for n in numbers:
        if n in unique_number:
            unique_number[n] += 1
        else:
            unique_number[n] = 1
    
    for n in unique_number:
        if unique_number[n] == 1:
            return n
           
array_1 = ([1, 2, 2, 3, 3, 4, 4])
array_2 = ([7, 8, 8, 9, 9, 10, 10])
array_3 = ([5, 6, 6, 7, 7, 8, 8, 5, 9])

print(find_unique(array_1))
print(find_unique(array_2))
print(find_unique(array_3))