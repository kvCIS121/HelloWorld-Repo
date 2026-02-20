# The normal human body temperature is 98.6F in Fahrenheit and 37C in Celsuis. Create a function
# that determines if the temp is considered a fever(anove normal body temperature) or not. temp will
# be measured in Fahrenheit and Celsuis.
# Notice: The F or C will always be the last character in the string.
# Examples:
#  is fever(” 99F”) → True,
#  is fever(” 37C”) → False,
#  is fever(” 98F”) → False

def is_fever(fn_input):
    characters = fn_input[-1]
    numbers = float(fn_input[0:-1])

    if characters == 'f' or characters == 'F':
        if numbers > 98.6:
            return 'you have a fever'
    elif characters == 'c' or characters == 'C':
        if numbers > 37.0:
            return 'you have a fever'
    else:
        return 'your temp is normal'
    
print(is_fever('105F'))