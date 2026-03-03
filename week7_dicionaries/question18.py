# 18. Write a function that takes a dictionary, called employee salaries, where the keys are employee names
# and the values are their salaries. The function should return a list of employees earning above a given
# salary.
    # Examples:
        # high_earners({ ”Alice”: 50000, ”Bob”: 75000, ”Charlie”: 100000}, 60000) → [ ”Bob”, ”Charlie”]
        # high_earners({ ”David”: 30000, ”Emma”: 45000, ”Frank”: 50000}, 40000) → [ ”Emma”, ”Frank”]
        # high_earners({ ”George”: 25000, ”Hannah”: 27000, ”Ian”: 29000}, 30000) → []

def income(employee_earnings, salaries):
    result = []

    for keys, values in employee_earnings.items():
        if values >= salaries:
            result.append(keys)
    return result

high_earners_1 = ({ 'alice': 50000, 'bob': 75000, 'charlie': 100000}, 60000)
high_earners_2 = ({ 'david': 30000, 'emma': 45000, 'frank': 50000}, 40000)
high_earners_3 = ({ 'george': 25000, 'hannah': 27000, 'ian': 29000}, 30000)

print(income(high_earners_1[0], high_earners_1[1]))
print(income(high_earners_2[0], high_earners_2[1]))
print(income(high_earners_3[0], high_earners_3[1]))
