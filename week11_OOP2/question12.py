class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        self.price = new_price
    
    def show_description(self):
        print(f'Name: {self.name}, Menu price: {self.price}')

    def __str__(self):
        return f'MenuItem(name = {self.name}, Price = {self.price})'

class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []

    def add_menu_item(self, item):
        self.menu_items.append(item)
            
    def display_menu(self):
        for item in self.menu_items:
            item.show_description()
    
    def lunch_menu(self):
        for item in self.menu_items:
            discounted_price = item.price - 2
            print(f'Name: {item.name}, Lunch Price: {discounted_price}')

    
    def __str__(self):
        return f'Restaurant(restaurant_name = {self.restaurant_name}, items = {len(self.menu_items)})'

#creating object for MenuItem
menu_item_1 = MenuItem('pasta', 25)
menu_item_2 = MenuItem('steak', 50)

#creating object for Restaurant
restaurant_1 = Restaurant('McDonalds')

#add MenuItems to the Restaurant 
restaurant_1.add_menu_item(menu_item_1)
restaurant_1.add_menu_item(menu_item_2)

#execute program
restaurant_1.display_menu()
restaurant_1.lunch_menu()
print(restaurant_1)
