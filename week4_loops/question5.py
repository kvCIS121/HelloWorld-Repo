#   Use a FOR LOOP for finding a factor b/c the factors are somewhere between 1 and the number itself
#   a factor is an integer that divides the input with no remainder
#   print(testing_each_number_from_one_to_itself, end = " ")
#   the range must have START, STOP / LOWER, UPPER limits of the number 1 and the number itself!
#   i need to increment by 1, starting from 0, to test each number against my user number to see if it's a factor thru division/multiplication

user_input = int(input('enter a number: '))
numbers_in_the_loop = 0


for number in range(1, user_input + 1):
     numbers_in_the_loop += 1
     if user_input % numbers_in_the_loop == 0:
         print(numbers_in_the_loop, end = ' ')
        