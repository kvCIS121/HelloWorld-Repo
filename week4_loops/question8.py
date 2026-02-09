#   Write a program that repeatedly asks the user for integers until a negative integer is given.
#   The program should keep track of the sum of the numbers and print the sum at the end
#   (not including the negative number)...

done = False
total_of_integers_entered = 0

while not done:
    integers_entered = int(input('enter a number (to stop, enter a negative number):'))
    
    if integers_entered < 0:
        print("this is a negative number, try again")
        break
    
    elif integers_entered >= 0:
        total_of_integers_entered += integers_entered
        
print(f'the sum of all integers entered is: {total_of_integers_entered}')