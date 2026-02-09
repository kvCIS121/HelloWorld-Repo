word2 = 'HAPPY ITMES'

print(word2[4:7])   #this ONLY prints a section/ specific index position of the word, which
                    #is why it only prints ONE time and the letters Y and I, which are index 4 and index 7

print(word2[4:7+1]) 

print(word2[6:10+1])    #dont do this b/c python knows we really dont have an index of 11

print(word2[4:])        #DO THIS INSTEAD. Leaving the STOP blank, it will go from index 4 all the way till end
print(word2[:7])        #Leaving the START blank, it will start at ZERO index and go till index #6 (recall 7 as a stop makes it exclusive)

# This is how slice works:  string[start : stop : step]