# 9. 
# Write a function named add_lists that takes two lists: lyst1 and lyst2 and adds the first element in lyst1
# with the first element in lyst2, the second element lyst1 with the second element lyst2, etc. Return a
# new list containing the corresponding sums of the list1 and list2. 
# You may assume both lists have the same length.
    # Examples:
        # add_lists([1, 3, 3, 1], [4, 3, 6, 1]) → [5, 6, 8, 2] ( since 1+4=5; 3+3=6; 3+6=9; 1+1=2)
        # add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6]) → [1, 1, 9, 2, -13]
        # add_lists([1, 2], [-1, 1]) → [0, 3]

def add_lists(list1, list2):
    
    result = []

    for i in range(len(list1)):

        result.append((list1[i] + list2[i]))

    return result

List_1_and_2 = [[1, 3, 3, 1] , [4, 3, 6, 1]]

print(add_lists(List_1_and_2[0], List_1_and_2[1]))
