#   Hailstone Sequence
#   Given a positive integer n, the following rules will always create a sequence that ends with 1

#   (a) If n is even, divide by 2
#   (b) If n is odd, multiply by 3 and add 1 (i.e. 3n + 1)
#   (c) Continue until n is 1

#   Write a program that prints the hailstone sequence starting at n = 25.

n = int(input('enter a number: '))
update_n = 0

while n != 1:   #set while n does not equal 1 b/c we want to loop till n = 1, which is Haistone sequence, when n ends at value of 1
    if n % 2 == 0:
        n = n // 2  #   use FLOOR DIVISION in order to keep ONLY whole number of result. ex: 7//3 = 2. Otherwise, 7/2 = 2.3333...
        
    elif n % 2 == 1:
        n = (3*n) + 1
        
print(n)

