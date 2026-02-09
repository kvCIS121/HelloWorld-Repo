#   Using a loop, write code to calculate the sum of all odd numbers between 50 and 517. Print the result.

iteration_count = 0
total = 0

for number in range(51, 517+1, 2):
    total += number # Total starts at zero. += means add the number to the total per iteration => 51 + 53 + 55 + n ...
    iteration_count += 1    # Add 1 to iteration_count each iteration to keep track of how many it takes
    
print(f'the number of iterations needed to calculate all odd numbers is {iteration_count}')
print(f'the sum of all odd numbers are: {total}')

#note: i put PRINT OUTSIDE of the FOR LOOP in order to NOT PRINT ALL 234 ITERATIONS that added the 
# numbers each time. if the PRINTS would've been inside, it would print each line, each time 
# that the total was being added to the next odd number. See below example:



#-----<>    This is the version that would print ALL the lines that iterate each time 
#           because the PRINT functions are insdie the FOR LOOPS

iteration_count = 0
total = 0

for number in range(51, 517+1, 2):
    total += number 
    iteration_count += 1    
    
    print(f'the number of iterations needed to calculate all odd numbers is {iteration_count}')
    print(f'the sum of all odd numbers are: {total}')
