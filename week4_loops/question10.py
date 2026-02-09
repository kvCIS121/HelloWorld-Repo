#   Write a program that repeatedly asks the user for integers until a negative integer is given.
#   Report back the largest even number the user entered (not including the negative number).
#   If the user didn’t enter any even numbers report back −1

largest_even_number = -1    #   i set this constant to -1 b/c anything above this will be considered, 
                            #   this is also when the loop stops since a negative number is entered

while True: #   This creates an infinite loop that will only stop when you explicitly break

    user_number = int(input('enter a number: '))

    if user_number >= 0:
        if user_number % 2 == 0:
            if user_number > largest_even_number:
                largest_even_number = user_number
            elif user_number < largest_even_number:
                largest_even_number = largest_even_number
        
       
    elif user_number <= -1:
        break

print(largest_even_number)