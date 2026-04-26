file = open('LibraryVisitsData.csv', 'r')

lines = file.readlines()

total = 0
count = 0

# Skip the header row
for line in lines[1:]:
    line = line.strip()          # remove newline
    if line == "":               # skip empty lines
        continue

    parts = line.split(',')      # split by comma
    visitors = int(parts[1])     # convert visitor count to integer

    total = total + visitors
    count = count + 1

# Prevent division by zero
if count > 0:
    average = total / count
    print("Average visitors per day:", average)
else:
    print("No data found in file.")

file.close()
