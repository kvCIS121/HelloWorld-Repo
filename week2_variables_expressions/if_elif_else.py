
user_age = int(input("What is your age: "))
if user_age < 3:
    ticket_price = 0
elif user_age >= 65:
    ticket_price = 100
else: 
    ticket_price = 10
print(ticket_price)

