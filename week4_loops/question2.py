#   For question number 2: Write a program that asks the user for a word and then, using a loop, prints every other letter of the
#   word starting with the second letter. We need to use operator LENGTH: LEN 
#   This loops safely from index of 0 to the LENGTH OF THE WORD


#   'happyday' index positions
#- 0 → h
#- 1 → a
#- 2 → p
#- 3 → p
#- 4 → y
#- 5 → d
#- 6 → a
#- 7 → y

#   Let word = 'happyday'; print(word[0]) = 'h'; this prints index 0, which is 'h': this is SLICING

#----<>
#   To write code for question two, use "char" in "userword[start:stop:step]" direclty 
# because "char" refers to STRING, and 'user_word' calls the string directly, this is not 
# an INTEGER. If it was, we would use: 
#   "for INDEX in RANGE(word(start, stop, step))"  <- notice the commas and paranthesis? 
#   This is different for STRING, where we call the STRING VARIABLE directly and have 
#   square brackets with COLONs to show START:STOP:STEP

user_word = input('enter a word: ')
for char in user_word[::]:  #   user_word[START: STOP] b/c i left START and STOP blank, it includes the whole word
    print(user_word[1::2])  #   user_word[START: STOP: STEP] STEP is to print every letter, by a step of 2, 
    break                   #   starting at 1 (it prints the letter index position 1), then every 2 steps
                            #   therefore, it'll print index positions 1,3,5,7 etc...
                            #   however, if i start at 0, it'll print index positions
                            #   0,2,4,6,8 etc
                            #   I used a FOR LOOP to print every other letter, but it'll also print 
                            #   the amount of times that there are letters in the word, so, 
                            #   to prevent that from happening, I used BREAK 

#-----<>

#   Alternate way to write this code without using a loop to iterate and having to use BREAK is:

user_word = input('enter a word: ')
print(user_word[1: :2])

#   This is a short cut to print exactly the index 1 of the word, and then each 2 steps till end of word