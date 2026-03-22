# 6. Given a positive integer n, the following rules will always create a sequence that ends with 1, called
# Hailstone Sequence:

# (a) If n is even, divide by 2
# (b) If n is odd, multiply by 3 and add 1 (i.e. 3n + 1)
# (c) Continue until n is 1

# Write a function that prints the hailstone sequence starting at n. The argument to the function will
# be n (the integer to start the sequence from), if no argument is provided then the default should be 40.

# Examples:
# hailstone_seq(25) → 25, 76, 38, 19, 58 ... 8, 4, 2, 1,
# hailstone_seq(40) → 40, 20, 10, 5, 16, 8, 4, 2, 1
# hailstone_seq( ) → 40, 20, 10, 5, 16, 8, 4, 2, 1

def hailstone_seq(n):
    
    print(n, end= ' ')
    while n != 1:
        if n % 2 == 0:
            n = n//2
            print(n, end=' ')
        else:
            n = (3*n) + 1
            print(n, end=' ')
    return n
    
number = int(input('enter a number: '))
print(hailstone_seq(number))