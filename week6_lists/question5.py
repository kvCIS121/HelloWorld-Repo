# 5. Given a positive integer n, the following rules will always create a sequence that ends with 1, called

# Hailstone Sequence:
    # (a) If n is even, divide by 2
    # (b) If n is odd, multiply by 3 and add 1 (i.e. 3n + 1)
    # (c) Continue until n is 1

# Write a function that returns a list with the hailstone sequence starting at n. The argument to the
# function will be n (the integer to start the sequence from). 

# Examples:
    # hailstone seq(25) → [25, 76, 38, 19, 58 ... 8, 4, 2, 1],
    # hailstone seq(40) → [40, 20, 10, 5, 16, 8, 4, 2, 1]


#<> Version 1: Printing results regularly, in horizontal

def hailstone_seq(fn_input):
    while fn_input != 1:

        if fn_input % 2 == 0:
            fn_input = fn_input//2
            print(fn_input, end=" ")

        elif fn_input % 2 == 1:
            fn_input = (3*fn_input)+1
            print(fn_input, end=" ")
    return fn_input

n = int(input('enter a number: '))
print(hailstone_seq(n))


#<> Version 2: Printing results into a List 

def hailstone_seq2(fn_input2):
    result2 = [fn_input2]   # setting result = [] in sqr bracket, w/ fn_input2 inside says i want results in List

    while fn_input2 != 1:
        if fn_input2 % 2 == 0:
            fn_input2 = fn_input2//2
            
        elif fn_input2 % 2 == 1:
            fn_input2 = (3*fn_input2)+1
            
        result2.append(fn_input2)
    return result2

n2 = int(input('enter number: '))
print(hailstone_seq2(n2))

