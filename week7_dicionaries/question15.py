# 15. Write a function named majority_element that takes a list of integers named nums and returns the
# majority element. 
# 
# The majority element is the element that has at least half of the occurrences. 
# You may assume that the majority element always exists and is unique.
    # 
    # Examples:
        # majority_elment([3,2,3]) → 3
        # majority_elment([2,2,1,1,1,2,2]) → 2
        # majority_elment([2,2,3,2,1,2,1,4,4,1,2,2]) → 2

def majority_element(lysts):
    result = {}

    for i in lysts:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1

    for i in result:
        if result[i] >= (len(lysts))//2:
            return i
#           return result => will return a dictionary of ea/ element and its occurence

nums_1 = ([3,2,3])
nums_2 = ([2,2,1,1,1,2,2])
nums_3 = ([2,2,3,2,1,2,1,4,4,1,2,2])

print(majority_element(nums_1))
print(majority_element(nums_2))
print(majority_element(nums_3))

# Note: - The majority element is defined as: count >= (length of the list)/ 2
# Notes:
#   i in lysts => i is the actual number within the lyst that its looping thru
#   result[i] => is how many times this specific number appears
#   
#   return result: will give me a dictionary of each element and how many 
#   times it actually appeared in a dictionary format, i.e. {3: 2, 2:1} for nums_1...

