# An Isogram is a word that has no duplicate letters. 
# Create a function that takes a string and returns
# either True or False depending on whether or not it is an” isogram”. 
# You may assume words will only
# have lower case letters

def isogram(fn_input):
    accumulator = ''

    for i in fn_input:
        if i in accumulator:
            return False
        accumulator = accumulator + i
    return True

word = 'duplicate'
print(isogram(word))

