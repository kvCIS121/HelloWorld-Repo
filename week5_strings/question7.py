# Professor Dumbledore seeks to decipher powerful encoded spells in the Hogwarts Library, their secrets
# revealed by the first letter of each word. Create a function called first letters that takes the variable
# sentence (a string) and returns a string made up of the first letters of each word in the sentence.

# Examples:
# first letters(”wingardium leviosa makes objects float”) → ”wlmof”
# first letters(”expecto patronum repels dementors”) → ”eprd”
# first letters(”the magic is within you”) → ”tmiwy”

def first_letters(fn_input):
    accumulator = sentence[0]
    for i in range(len(fn_input)):
        if fn_input[i] == ' ':
            accumulator = accumulator + sentence[i+1]

    return accumulator

sentence = 'wingardium leviosa makes objects frog'
print(first_letters(sentence))
