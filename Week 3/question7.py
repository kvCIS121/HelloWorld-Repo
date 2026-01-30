## ---------------> Version 1
learning = input('Enter a letter: ')
vowels = ('a,e,i,o,u')
consonants = ('b,c,d,e,f')

if learning in vowels: # using "in" checks whether the input entered is within a certain group, in this case, Vowels
    print(f'Your letter {learning} is a vowel')
elif learning in consonants: # using "in" checks whether the input entered is within a certain group, in this case, Consonants
    print(f'Your letter {learning} is a consonant')

# Note: "in" was learned using Microsoft CoPilot AI

## ---------------> Version 2

learning_2 = input('Enter a letter: ')
vowels_2 = ('a, e, i, o, u')
consonants_2 = ('b, c, d, e, f')  

if learning_2 == 'a' or learning_2 == 'e' or learning_2 == 'i' or learning_2 == 'o' or learning_2 == 'u':
    print(f'Wow! The letter {learning_2} is a Vowel!')
elif learning_2 == 'b' or learning_2 == 'c' or learning_2 == 'd' or learning_2 == 'e' or learning_2 == 'f':
    print(f'Wow! The letter {learning_2} is a Consonant!')

# This version is without having learned about the "in" use for checking inside a group for a particular integers or strings