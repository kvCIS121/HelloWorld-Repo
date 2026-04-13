class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        self.price = new_price
    
    def display_details(self):
        print(f'Product name: {self.name}, Product price: {self.price}')
    
    def __str__(self):
        return f'Product(name = {self.name}, price = {self.price})'

class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def __str__(self):
        return f'ShoppingCart(customer_id = {self.customer_id})'

#creating product object
product_1 = Product('Shoes', 100)
product_2 = Product('clothes', 100)
product_3 = Product('food', 300)

#creating shoppingcart object
shoppingcart_1 = ShoppingCart('Cart #1717')

#adding product to the shopping cart
shoppingcart_1.add_product(product_1)
shoppingcart_1.add_product(product_2)
shoppingcart_1.add_product(product_3)

#executing program
shoppingcart_1.calculate_total()
print(shoppingcart_1.calculate_total())
print(shoppingcart_1)
