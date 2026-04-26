file1 = open('LunchData.txt', 'r')
file2 = open('TotalLunchSered', 'w')

lunch = file1.readlines()

total = 0
for line in lunch:
    date = line.split() 
    number = int(date[1])
    total = total + number

file2.write('Total lunches served last year was: ' + str(total))
file1.close()
file2.close()