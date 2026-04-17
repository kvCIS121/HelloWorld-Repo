class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self,item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def __add__(self,other):
        new_cart = ShoppingCart()

        for item, quantity in self.items.items():
            new_cart.items[item] = quantity
        
        for item, quantity in other.items.items():
            if item in new_cart.items:
                new_cart.items[item] += quantity
            else:
                new_cart.items[item] = quantity
        return new_cart
    
    def __str__(self):
        return str(self.items)

p1 = ShoppingCart()
p1.add_item('tea')
p1.add_item('energy drink')
p1.add_item('energy drink')

p2 = ShoppingCart()
p2.add_item('energy drink')
p2.add_item('energy drink')
p2.add_item('energy drink')
p2.add_item('hat')

p_sum = p1+p2
print(p_sum)        