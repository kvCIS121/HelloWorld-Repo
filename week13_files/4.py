file_1 = open('MyWords.txt', 'r')
file_2 = open('NewFile.txt', 'w')

words = file_1.readlines()

#LINE 1
lyst = []
for word in words[0:5]:
    lyst.append(word.strip())#remove newline

eachLine = ''
for word in lyst:
    eachLine = eachLine + word + ", "
file_2.write(eachLine + '\n')

#LINE 2
lyst = []
for word in words[6:11]:
    lyst.append(word.strip())#remove newline

eachLine = ''
for word in lyst:
    eachLine = eachLine + word + ", "
file_2.write(eachLine + '\n')

#LINE 3
lyst = []
for word in words[12:17]:
    lyst.append(word.strip())#remove newline

eachLine = ''
for word in lyst:
    eachLine = eachLine + word + ", "
file_2.write(eachLine + '\n')

#LINE 4
lyst = []
for word in words[18:23]:
    lyst.append(word.strip())#remove newline

eachLine = ''
for word in lyst:
    eachLine = eachLine + word + ", "
file_2.write(eachLine + '\n')

file_1.close()
file_2.close()