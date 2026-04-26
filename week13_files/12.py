file1 = open('DailyTemperatures.csv', 'r')

lines = file1.readlines()

temperatures = []

for line in lines[1:]:
    line = line.strip()
    if line == '':
        continue

    parts = line.split(',')
    temp = int(parts[1])

    temperatures.append(temp)

file1.close()

highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

total = 0
count = 0

for temp in temperatures:
    total = total + temp
    count = count + 1

average = total / count

print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Average temperature:", average)


