# 16. Write a function that takes a dictionary called names of tech ids and student names as key-value
# pairs, and returns a list containing just the student names.
    # Examples:
        # get_names({ ”01475”: ”Steve”, ”87469”: ”Alice”, ”654123”: ”Bob” })→[ ”Steve”, ”Alice”, ”Bob”]
        # get_names({ ”ID1”: ”John”, ”ID2”: ”Emma”, ”ID3”: ”Liam” }) → [ ”John”, ”Emma”, ”Liam”]
        # get_names({}) → []

def names(student_names):
    result = []

    for values in student_names.values():
        result.append(values)
        
    return result

names_1 = ({ '01475': 'steve', '87469': 'alice', '654123': 'bob' })
names_2 = ({ 'ID1': 'john', 'ID2': 'emma', 'ID3': 'liam' })
names_3 = ({})

print(names(names_1))
print(names(names_2))
print(names(names_3))