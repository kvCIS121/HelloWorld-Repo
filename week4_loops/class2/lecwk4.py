#USING TRUE/ FALSE WITH FOR LOOP
#determine if the following word has the letter 'a'
word1 = 'tabelspoonful'
word2 = 'technology'

a_appears = False
for letter in word2:
    if letter == 'a':
        a_appears = True
        break #this means that if we ever find an 'a' in the word, just stop and no longer run code

if a_appears:
    print(f'yes, the word {word1} has an a')
else:
    print(f'no, the word {word1} does not have an a')


#+++++


#Using DONE = FALSE
#determine if the following word has the letter 'a'

word1 = 'tabelspoonful'
word2 = 'technology'
a_appears = False
done = False


while not done:
    if letter == 'a':
        done = True
        break #this means that if we ever find an 'a' in the word, just stop and no longer run code

if a_appears:
    print(f'yes, the word {word1} has an a')
else:
    print(f'no, the word {word1} does not have an a')


#+++++

# 'm' + 'a' is not the same as 3+4; 'm' + 'a' is concactanation. Its 'stringy', saying to put the 
# string letters m and a together.

int x = 3
str y = 'apple'

# variable y points to the word 'apple'
# apple has 5 letters, and starting at 0, it will go up to 4, for number of spots,
# machine has 0-based index. It starts at zero. therefore, A P P L E = 0,1,2,3,4

# INDEXING

