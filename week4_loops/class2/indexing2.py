
word2 = 'HAPPY TIMES'
for index in range(0,7+1):  #this only prints up to index of 7. If the word had more, it wouldn't work, it'll say there's an error
    print(word2[index])
    

word3 = input('enter a word: ')

for index in range(0, len(word3)):  #this prints whole length of word w/o having to know how many index positions
    print(word3)


word1 = input('enter a word: ')
result = word1

for index in range(0, len(word1)):  
    print(result)   #this helps print result on one horizontal line, but it will go thru the iterations as many times as there are letters
    
#   using LENGTH, LEN let's us print all the indexes of the whole word w/o
#   having to know the amount of indexes it contains

