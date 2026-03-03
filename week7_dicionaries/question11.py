# 11. Write a function that takes a dictionary, called sales, 
# where the keys are product names and the
# values are the number of units sold. 
# The function should return the total number of products sold.
    # Examples:
        # total_sales({ ”Laptop”: 5, ”Phone”: 10, ”Tablet”: 3}) → 18
        # total_sales({ ”Shoes”: 20, ”Hats”: 15, ”Jackets”: 10}) → 45
        # total_sales({ ”Book”: 1, ”Pen”: 2, ”Notebook”: 1}) → 4

def total_products_sold(sales):
    total_sold = 0
       
    for product_names, units_sold in sales.items():
        total_sold = total_sold + units_sold
       
    return total_sold

sales_1 = ({ '”Laptop”': 5, '”Phone”': 10, '”Tablet”': 3})
sales_2 = ({ '”Shoes”': 20, '”Hats”': 15, '”Jackets”': 10})
sales_3 = ({ '”Book”': 1, '”Pen”': 2, '”Notebook”': 1})

print(total_products_sold(sales_1))
print(total_products_sold(sales_2))
print(total_products_sold(sales_3))