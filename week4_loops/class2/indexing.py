x = 'apple'

#square brackets tells python to get a letter stored at the index indicated,
# [0][1][2][3][4] => a p p l e 

x = 'apple'


#write code to print the letter 'L' 'l'

word1 = 'APPLE'

word2 = 'HAPPY TIMES'

print(word2[3]) #CODE TO PRINT L
print(word2[4]) #code to print y
print(word2[5]) 
print(word2[6]) #code to print t; note, it's index 6 b/c we had to include the SPACE as an index position too. SPACE is a considered a "letter"
print(word2[7])
print(word2[8])

#instead of repeating the same process of printing each letter separately, use a FOR LOOP

word1 = 'APPLE'

word2 = 'HAPPY TIMES'
for index in range(4,7+1):
    print(word2[index])