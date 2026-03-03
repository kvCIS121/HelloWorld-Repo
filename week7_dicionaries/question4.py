# 4. Write a function that takes a dictionary, called people, 
# containing the names and ages of a group of
# people, and returns the name of the youngest person.
    # Examples:
        # find_youngest({ ”Emma”: 71, ”Jack”: 45, ”Olivia”: 82, ”Liam”: 39}) → ”Liam”
        # find_youngest({ ”Sophia”: 50, ”Mason”: 68, ”Ava”: 67, ”Noah”: 33}) → ”Noah”
        # find_youngest({ ”Ethan”: 25, ”Lucas”: 30, ”Mia”: 29}) → ”Ethan”

def find_youngest(people):
    youngest_person = ' '
    youngest_age = 100

    for current_person, current_age in people.items():
        if current_age < youngest_age:
            youngest_age = current_age
            youngest_person = current_person
    return {youngest_person:youngest_age}

people_1 = ({ '”Emma”': 71, '”Jack”': 45, '”Olivia”': 82, '”Liam”': 39})
people_2 = ({ '”Sophia”': 50, '”Mason”': 68, '”Ava”': 67, '”Noah”': 33})
people_3 = ({ '”Ethan”': 25, '”Lucas”': 30, '”Mia”': 29})

print(find_youngest(people_1))
print(find_youngest(people_2))
print(find_youngest(people_3))