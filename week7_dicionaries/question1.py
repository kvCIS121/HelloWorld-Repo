# 1. Write a function that takes a dictionary, called people, containing the names and ages of a group of
# people, and returns the name of the oldest person.
#   Examples:
        # find_oldest({ ”Emma”: 71, ”Jack”: 45, ”Olivia”: 82, ”Liam”: 39}) → ”Olivia”
        # find_oldest({ ”Sophia”: 50, ”Mason”: 68, ”Ava”: 67, ”Noah”: 33}) → ”Mason”
        # find_oldest({ ”Ethan”: 25, ”Lucas”: 30, ”Mia”: 29}) → ”Lucas”

def find_oldest(people):
    oldest_person = ' '
    oldest_age = -1
    
    for current_person, current_age in people.items():
        if current_age > oldest_age:
            oldest_age = current_age
            oldest_person = current_person
    directory = {oldest_person: oldest_age}
    return directory

group_1 = ({ '”Emma”': 71, '”Jack”': 45, '”Olivia”': 82, '”Liam”': 39})
group_2 = ({ '”Sophia”': 50, '”Mason”': 68, '”Ava”': 67, '”Noah”': 33})
group_3 = ({ '”Ethan”': 25, '”Lucas”': 30, '”Mia”': 29})

print(find_oldest(group_1))
print(find_oldest(group_2))
print(find_oldest(group_3))