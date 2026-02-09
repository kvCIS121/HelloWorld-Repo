#   Write a program that asks the user for an integer. Calculate (and then print) 
#   the sum of all square numbers up to and including the user input

user_input = int(input('enter a number: '))
numbers_in_sequence = 0 #this will be my counter that sequences from 0 up to user_input, that'll be sqr'd ea/ time
total_of_sqrd_numbers = 0

for number in range(0, user_input + 1):
    
    
    if number <= user_input:
        total_of_sqrd_numbers += number**2  #use NUMBER**2 (number squared) b/c number == 0, and it will be the sequence in the range up to the user_input

    #   print(numbers_in_sequence **2, end = " ")
    #   note: if i use this print, which is inside the loop, it will print the total of each iteration separately
print(f"the sum of all sqr'd numbers of {user_input} is: {total_of_sqrd_numbers}")  #this prints one time, at the end, summing all sqr's, b/c it's outside the loop

#   originally, I was going to use a counter (numbers_in_sequence) to help count up ea/ 
#   time to use as the squares, however, i don't need it b/c the range is already considering 
#   and counting for me. it already includes ea/ number in the range starting at 0 and up 
#   to the user_input number. so, I just need to use TOTAL_OF_SQRD_NUMBERS to sum up ea/ 
#   number that comes up in sequence per iteration 

#   Note: printing inside the loop will print each iteration results immediately, 
#   so, to print only one result one time, print outside the loop at the end