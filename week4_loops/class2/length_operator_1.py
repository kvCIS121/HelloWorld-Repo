
# TOPIC: Length = len
# len - reports the length of an object (the word)

vowels = 'aeiouyw'

print(len(vowels))
print(f'the number of vowels are: {len(vowels)}')

#LEN, length operator REPORTS the values of the word, which is 11, not the index letter of that position,
#which is why it prints 11 and not the word = 'HAPPY TIMES'; HAPPY TIMES = 11 LENGTHS

for index in range(0, len(vowels)-1):    #the minus 1 does not include the 's'
    print(index, vowels[index])





