def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}
    
    for word in words:
        reversed_word = ''
        #reverse the word and check if it is the orginal word
        for letter in word:
            reversed_word = letter + reversed_word
        if word == reversed_word:
            result["palindrome"].append(word)
        else:
            result["non-palindrome"].append(word)
                
    return result

# Test the function with a sample input
print(palindromes(["madam", "racecar", "hello", "level", "python"]))
# Expected output: {'palindrome': ['madam', 'racecar', 'level'], 'non-palindrome': ['hello', 'python']}

#print(palindromes(["noon", "civic", "deed", "open", "loop"]))
# Expected output: {'palindrome': ['noon', 'civic', 'deed'], 'non-palindrome': ['open', 'loop']}

#print(palindromes(["apple", "banana", "cherry"]))
# Expected output: {'palindrome': [], 'non-palindrome': ['apple', 'banana', 'cherry']}