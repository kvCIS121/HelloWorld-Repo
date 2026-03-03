# 6. An isogram is a word that has no duplicate letters. 
# Write a function that takes a string word and
# returns either True or False depending on whether or not it’s an isogram.
#   Examples:
    # is_isogram( ”algorism”) → True
    # is_isogram( ”password”) → False
    # is_isogram( ”consecutive”) → False

def is_isogram(word):
    accumulator = ' '

    for i in word:
        if i in accumulator:
            return False
        accumulator = accumulator + i
    return True

word1 = 'algorism'
word2 = 'password'
word3 = 'consecutive'

print(is_isogram(word1))
print(is_isogram(word2))
print(is_isogram(word3))