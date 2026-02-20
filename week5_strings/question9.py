# Write a function called flip flop that takes a string as an argument and returns a new word made up
# of the second half of the word first combined with the first half of the word second.
# Examples:
# flip flop(”abcd”) → ”cdab” (that is, ”cd” then ”ab” ...even length)
# flip flop(”grapes”) → ”pesgra” (that is, ”pes” then ”gra” ...even length)
# flip flop(”abcde”)→ ”decab” (that is, ”de” then ”c” then ”ab” ...odd length)
# flip flop(”cranberries”)→ ”rriesecranb” (that is, ”rries” then ”e” then ”cranb” ...odd length)

def flip_flop(fn_input):
    last_half = fn_input[ : len(fn_input)//2 : -1]
    middle_half = fn_input[len(fn_input)//2 :len(fn_input)//2 : ]
    first_half = fn_input[0 : len(fn_input)//2 : ]

    return last_half + middle_half + first_half

word = 'cranberries'    # → ”rriesecranb”
print(flip_flop(word))

# When slicing backward:
# - Leave the start empty to start at the end.
# - Provide a stop index where you want to stop.
# - Use -1 as the step.

# Note: 
# by using =>     "len(fn_input)//2", 
#
# im doing floor division to divide the 
# length of the string by half evenly for the 'MIDDLE_HALF' 
# index b/c I don't necessarily know where
# the middle will be for random strings, which can be anywhere from 5 to 5000 characters long...