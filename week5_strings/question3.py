# The boiling point of water is 212F in Fahrenheit and 100C in Celsuis. Create a function that
# determines if the temp is considered boiling or not. temp will be measured in Fahrenheit and Celsuis.
# Notice: The F or C will always be the last character in the string

def boiling_point(fn_input):
    characters = fn_input[-1]
    numbers = float(fn_input[0:-1])

    if characters == 'f' or characters == 'F':
        if numbers >= 212:
            return 'this is boiling point'
    elif characters == 'f' or characters == 'F':
        if numbers >= 100:
            return 'this is boiling point'
    else:
        return 'this is NOT boiling point'

print(boiling_point('500F'))