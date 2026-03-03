# 17. Write a function that takes a dictionary, called store, representing items and their prices, and an
# integer, called wallet, representing the amount of money you have. 
# 
# The function should return a list
# of items you can afford. 
# 
# If you cannot afford anything, return an empty list.
#   Examples:
        # items_purchase({ ”Water”: 1, ”Bread”: 3, ”TV”: 1000}, 300) → [ ”Bread”, ”Water”]
        # items_purchase({ ”Apple”: 4, ”Pan”: 100, ”Spoon”: 2 }, 100) → [ ”Apple”, ”Pan”, ”Spoon”]
        # items_purchase({ ”Phone”: 999, ”Laptop”: 5000, ”PC”: 1200 }, 1) → []

def can_afford(store, wallet):
    result = []
    
    for item, price in store.items():
        if price <= wallet:
            result.append(item)
    return result

   
items_purchase_1 = ({ 'water': 1, 'bread': 3, 'tv': 1000}, 300)
items_purchase_2 = ({ 'apple': 4, 'pan': 100, 'spoon': 2}, 100)
items_purchase_3 = ({ 'phone': 999, 'laptop': 5000, 'pc': 1200}, 1)

print(can_afford(items_purchase_1[0], items_purchase_1[1]))
print(can_afford(items_purchase_2[0], items_purchase_2[1]))
print(can_afford(items_purchase_3[0], items_purchase_3[1]))