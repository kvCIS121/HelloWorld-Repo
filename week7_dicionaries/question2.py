# 2. Write a function that takes a string word and returns a dictionary containing the count of each letter
# in the word.
# 
# Examples:
#   letter_count(” hello”) → {” h”: 1,” e”: 1,” l”: 2,” o”: 1}
#   letter_count(” mississippi”) → {” m”: 1,” i”: 4,” s”: 4,” p”: 2}
#   letter_count(” apple”) → {” a”: 1,” p”: 2,” l”: 1,” e”: 1}

def letter_count(word):
    dictionary = {}

    for i in word:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

word_1 = ('hello')
word_2 = ('mississippi')
word_3 = ('apple')

print(letter_count(word_1))
print(letter_count(word_2))
print(letter_count(word_3))