# 9. Below is a receipt from my recent lunch order.
    # (a) Initialize an empty dictionary named receipt, and then add the contents of the receipt as key-value pairs.
    # 
    # (b) Using the dictionary you created in part a, write code that prints the total cost of all the items
    # on the receipt. The code should work regardless of the contents of the receipt. (meaning don’t
    # write print(6+12+3))
        # 
        # Item Price
        # Side_Salad $6
        # Chicken_Parm $12
        # Cookie $3

receipt = {}
receipt['side salad']=6
receipt['chicken parm']=12
receipt['cookie']=3

def total_of_foods(receipt):
    total_cost = 0
    total_foods = ' '

    for pending_foods, pending_costs in receipt.items():
        total_cost = total_cost + pending_costs
    return total_cost

print(total_of_foods(receipt))