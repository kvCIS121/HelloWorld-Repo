# 2. Write a function that loops through a word and returns a list with every other letter of the word
# starting with the second letter. The function will take a single argument word (a string representing
# the word to process).

# Examples:
# skip letter( ”counterattack”) → [ ”o”, ”n”, ”e”, ”a”, ”t”, ”c”]
# skip letter( ”banana sunday”) → [ ”a”, ”a”, ”a”, ”s”, ”n”, ”a”]

# Version 1: using ".append(fn_input[i])"

def skip_letter(fn_input):
    result = []

    for i in range(1, len(fn_input), 2):
        result.append(fn_input[i])
    return result

word = 'counterattack'
print(skip_letter(word))

# Version 2: 

def skip_letter_2(fn_input_2):
    result_2 = []

    for i in range(1, len(fn_input_2), 2):
        result_2 = result_2 + [fn_input_2[i]]
    return result_2

word_2 = 'counterattack'
print(skip_letter_2(word_2))