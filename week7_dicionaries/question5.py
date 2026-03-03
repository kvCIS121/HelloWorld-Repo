# 5. Write a function that takes a list, called elements, and 
# returns a dictionary detailing how many times each element is repeated.
    # Examples:
        # count_repetitions([ ”cat”, ”dog”, ”cat”, ”cow”, ”cow”, ”cow”]) → { ”cow”: 3, ”cat”: 2, ”dog”: 1 }
        # count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]) → { 0: 6, 5: 3, 12: 2, 1: 1 }
        # count_repetitions([ ”Infinity”, ”null”, ”Infinity”, ”null”, ”null”]) → { ”null”: 3, ”Infinity”: 2 }

def count_repetitions(elements):
    dictionary = {}

    for i in elements:              # the the list or string called ELEMENTS, pull out one element at a time, call that element i
        if i in dictionary:         # "Have I seen this letter before?"
            dictionary[i] += 1      # "increase the count for this letter by 1, if yes"
        else:
            dictionary[i] = 1       # "this is first time seeing this letter, start its count by 1"
    return dictionary

elements_1 = ([ '”cat”', '”dog”', '”cat”', '”cow”', '”cow”', '”cow”'])
elements_2 = ([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0])
elements_3 = ([ '”Infinity”', '”null”', '”Infinity”', '”null”', '”null”'])

print(count_repetitions(elements_1))
print(count_repetitions(elements_2))
print(count_repetitions(elements_3))