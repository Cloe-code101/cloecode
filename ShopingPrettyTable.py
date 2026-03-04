#08/25/2025
# pretty table for shoping list for ramen

items=[]  # ingridients
amount=[] # amoun of ingredients
price=[]  # how much they cost

items_=""
amount_=0
price_=0

while (items_!= "done"):
    items_ = input("Enter item ")
    if items_ == "done":
        break
    else:
        items.append(items_)


    amount_ = input("Enter the amount ")
    amount.append(amount_)

    price_ = float(input("Enter the cost "))
    price.append(price_)

from prettytable import PrettyTable
table = PrettyTable()

table.field_names= ["Items", "Amount Needed", "price"]

for index in range(len(items)):
    table.add_row([items[index], amount[index], price[index]])
