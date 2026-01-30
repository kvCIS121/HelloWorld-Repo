number = 5

while number <= 100:
    if number % 2 == 0:
        print(number)
    number = number + 1

while number <= 100:
    if number % 2 == 0:
        print(number)
    number += 1


# x = 4
# x = x + 1
#   shorthand way to write: x += 1 (python notation)
# Example 2: x = x * 2 <=> x *= 2


#add up all the numbers between 7 and 50 (inclusively: means include ALL integers between 7 to 50, including 7 and 50)
num = 7
total = 0

while num <= 50:
    total += num
    num += 1

print(f'total = {total}')

#add up all the numbers between 7 and 50 (exclusively: means do NOT include the endpoints, which are 7 and 50)

num = 7
total = 0

while num < 50:
    total += num
    num += 1

print(f'total = {total}')