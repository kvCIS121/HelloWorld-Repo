file1 = open('ScienceFairVisitors.txt', 'r')
file2 = open('TotalVisitorsRecorded.txt', 'w')

lines = file1.readlines()

header = lines[0].strip()
print(header)

total = 0
for line in lines[1:]: #skips header row
    line = line.strip()
    if line == '':
        continue

    date = line.split() # ["1/1/25", "120"]
    number = int(date[1])   #convert visitor count to integer
    total = total + number

file2.write('Total number of visitors: ' + str(total))
file1.close()
file2.close()