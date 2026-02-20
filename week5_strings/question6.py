# A fruit juice company tags their fruit juices by concatenating the first three letters of the words in
# a flavor’s name, with its capacity. Create a function that creates product IDs for different fruit juices.
# Notice that the first input is a string and the second is an integer.

def product_id(flavor, capacity):
    first_three_letters = flavor[0:3]
    numbers = str(capacity)

    return first_three_letters + numbers

id1 = ('apple', 500)
id2 = ('orange', 1000)
id3 = ('grape', 1500)

print(product_id(id1[0], id1[1]))
print(product_id(id2[0], id2[1]))
print(product_id(id3[0], id3[1]))