# Let s be a string and words be a list of strings. The string s is considered an acronym of words if
# it can be formed by concatenating the first character of each string in words in order. 

# For example,
# "ab" can be formed from ["apple", "banana"], but it can’t be formed from ["bear", "aardvark"].

# Write a function that takes a string s and a list of strings words, and returns True if s is an acronym
# of words, and False otherwise


def is_an_acronym(s_string, word_list):
    result = []
    for index in range(len(word_list)):
       if s_string[index] != word_list[index][0]:
          return False
    return True
string_of_acronyms = 'ab'
list_of_words = ['apple', 'banana']

print(is_an_acronym(string_of_acronyms, list_of_words))