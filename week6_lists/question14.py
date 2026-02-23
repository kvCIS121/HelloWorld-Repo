# 14. 
# Write a function that takes two numbers as arguments num and length and returns a list of multiples
# of num until the list length reaches length.
#   Examples:
        # list_of_multiples(7, 5) → [7, 14, 21, 28, 35]
        # list_of_multiples(12, 10) → [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
        # list_of_multiples(17, 6) → [17, 34, 51, 68, 85, 102]`

def list_of_multiples(num, length):
    result = []

    for i in range(1, length + 1):  # i starts at i = 1, stops at length + 1 = 5. 
        result.append(num * i) # the value of num * i gets executed and stored in the list
    return result

LOM_1 = (7, 5)
LOM_2 = (12, 10)
LOM_3 = (17, 6)

print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))

