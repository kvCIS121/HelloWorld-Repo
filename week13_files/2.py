file1 = open('thisFile.txt', 'r')
file2 = open('thatFile.txt', 'w')

everyOtherLine = file1.readlines()

for lines in range(0, len(everyOtherLine), 2):
    file2.write(everyOtherLine[lines])

file1.close()
file2.close()