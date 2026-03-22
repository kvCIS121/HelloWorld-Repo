# 13. Write a function named is_vowel that returns a boolean value which determines if an letter is a vowel.
# Write a second function named report_vowels that takes a string and returns a list containing all the
# vowels from the original string. Call the is vowel function as part of the report_vowels function.

# Hint: In the English language, the letters a, e, i, o, and u are the vowels.
     
    # Examples:
    # report_vowels( ”apple”) → [a,e]
    # report_vowels( ”banana”) → [a,a,a]
    # report_vowels( ”run time error”) → [r,i,e,e,o]

def is_vowels(letters):

    if letters in 'aeiou':
        return True
    else:
        return False

def report_vowels(word):
    
    result = []
    
    for char in word:
        if is_vowels(char):
            result.append(char)
    return result

word = 'apple'
letters = input('enter a letter: ')

print(is_vowels(letters))
print(report_vowels(word))
