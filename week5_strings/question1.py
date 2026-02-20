# Zyra the code mage has hidden a mysterious cipher in reversed messages. You must help Zyra uncover
# the secrets of the digital realm. Create a function called reverse string that takes the variable word
# (a string) and returns the word in reversed order.
# For this problem, you must use iteration (a loop) not slicing.

def reversed_string(fn_input):
    word_reversed = " "
    for i in fn_input:
        word_reversed = i + word_reversed
    return word_reversed

word = 'programming'
print(reversed_string(word))