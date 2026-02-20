# Severus Snape seeks to harness powerful spells in the Hogwarts Library, you must encode them by
# using the last letter of each word. Create a function called last letters that takes the variable sentence
# (a string) and returns a string made up of the last letters of each word in the sentence

# note: the current letter being iterated thru is the last letter when compiler 
# understands that the next letter is a space (empty)

def last_letters(input_sentence):
    last_letters = ""
    input_sentence = input_sentence + " "   
    # keep in mind, ensure there's a space in between the quotations b/c that's what we're doing to let compiler 
    # know it's the last letter in our if-statement in line 15

    for i in range(len(input_sentence)-1):
        if input_sentence[i + 1] == " ":
            last_letters = last_letters + input_sentence[i]
           
    return last_letters

input = 'wingardium leviosa makes objects float'
print(last_letters(input))
