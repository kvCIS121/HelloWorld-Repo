#   even_printer is just the name of the function, nothing more
#   - start and stop are parameters—placeholders for the numbers you’ll pass in (like 2 and 10).


def even_printer(start, stop):  # - This line says: “I’m defining a function that will print even numbers between start and stop.”
    for number in range(start, stop + 1):   #   - for number in range(start, stop + 1): creates a loop.
        if number % 2 == 0: #- number % 2 == 0 means “number is divisible by 2 with no remainder”—that’s the definition of an even number.
            print(number)   # - If the if condition is true, this line runs.

#   Function calls
#   we're trying to call each set of numbers here
even_printer(2, 10) #   first set, call between 2 to 10, each even number considering they can modulus 2 and have a remainder == 0
even_printer(3, 15) #   next is this set, checks each number 3 to 15, each number that can modulus with 2 and have remainder == 0 prints
even_printer(7, 20) #   ...

#   