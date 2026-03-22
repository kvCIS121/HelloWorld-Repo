# 11. Write a function that takes two numbers as arguments num and length and returns a list of multiples
# of num until the list length reaches length, if no argument is provided then the default for the list
# length should be 5.
    # 
    # Examples:
    # list_of_multiples(7, 5) → [7, 14, 21, 28, 35]
    # list_of_multiples(12, 10) → [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    # list_of_multiples(2) → [2, 4, 6, 8, 10]
    # list_of_multiples(2,3) → [2, 4, 6]

def lyst_of_multiples(num, length = 5):
    result = []

    for n in range(1, length + 1):
        result.append(n * num)

    return result

lyst_1 = (7,5)
lyst_2 = (12,10)
lyst_3 = (2,)
lyst_4 = (2,3)

print(lyst_of_multiples(lyst_1[0], lyst_1[1]))
print(lyst_of_multiples(lyst_2[0], lyst_2[1]))
print(lyst_of_multiples(lyst_3[0], ))
print(lyst_of_multiples(lyst_4[0], lyst_4[1]))