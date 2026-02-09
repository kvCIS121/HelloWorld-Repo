#   This question uses: Concatenating
    #   Concatenating means “joining strings together into one longer string.”
    #   you are concatenating the new input onto the end of the existing string.
    # Examples
    # - "a" + "b" → "ab"
    # - "hello" + "world" → "helloworld"
    # - "" + "x" + "y" + "z" → "xyz"



#   Write a program to create a word one letter at a time. 
#   You should prompt the user to enter a single
#   letter one at a time until they type "done". 
#   Once they type "done", output their newly created word as an entire STRING (concatenating).

done = False
string_of_each_letter = " " #   This is adding the strings of ea/ input letter together, sorta
                            #   like saying TOTAL = 0, and then TOTAL += number meaning, 
                            #   add the next number in sequence to the previously stored total...

while not done:
    user_input = input('enter a letter (or type "done"): ')
    
    if user_input == 'done':
        break
    elif user_input != 'done':
        string_of_each_letter += user_input #   adding the string of ea/ input letter to total..
print(string_of_each_letter)    #   print outside of loop prints one time, and prints entire string total/ concatenation combined

    
