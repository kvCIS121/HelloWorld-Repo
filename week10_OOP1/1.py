# 1. Create an Product class.
# A product has
#  A name
#  A price
#  A quantity

class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
    def get_quantity(self):
        return self._quantity
    
    def set_name(self, new_name):
        self._name = new_name
    def set_price(self, new_price):
        self._price = new_price
    def set_quantity(self, new_quantity):
        self._quantity = new_quantity
    
food1 = Product('orange', 5, 20)

print(food1.get_name())
print(food1.get_price())
print(food1.get_quantity())


# Changing the name. Initial: orange, changed to: 'grapes'
food1.set_name('grapes')
print(food1.get_name())

# Chaning the price. Initial: 5, changed to: $10
food1.set_price(10)
print(food1.get_price())

# changing the quantity. Initial: 20, changed to: 55
food1.set_quantity(55)
print(food1.get_quantity())

