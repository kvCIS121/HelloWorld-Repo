file1 = open('CaloriesBurnedData.txt', 'r')
file2 = open('HighestNumberCalories.txt', 'w')

lines = file1.readlines()

highest = 0
highest_date = ""

for day in lines:
    day = day.strip()
    if day == "":
        continue

    parts = day.split()          # split by spaces
    date = parts[0]
    calories = int(parts[1])

    if calories > highest:
        highest = calories
        highest_date = date

file2.write("Day with highest calories burned: " + highest_date + "\n")
file2.write("Calories burned: " + str(highest))

file1.close()
file2.close()
