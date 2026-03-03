# 12. Write a function that takes a dictionary, called donations, where the keys are donor names and the
# values are the amount donated. The function should return the total amount donated.
    # Examples:
        # total_donations({ ”John”: 100, ”Sarah”: 200, ”Mike”: 50}) → 350
        # total_donations({ ”Anna”: 500, ”Tom”: 1000, ”Jerry”: 1500}) → 3000
        # total_donations({ ”Chris”: 25, ”Alex”: 30, ”Morgan”: 45}) → 100

def total_donations(donations):
    total_amount_donated = 0

    for donor_names, amount_donated in donations.items():
        total_amount_donated = total_amount_donated + amount_donated
    return total_amount_donated

donations_1 = ({ 'john': 100, 'sarah': 200, 'mike': 50})
donations_2 = ({ 'anna': 500, 'tom': 1000, 'jerry': 1500})
donations_3 = ({ 'chris': 25, 'alex': 30, 'morgan': 45})

print(total_donations(donations_1))
print(total_donations(donations_2))
print(total_donations(donations_3))
