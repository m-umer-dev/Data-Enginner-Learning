products = [
    {"name": "Charger", "price": 800},
    {"name": "Earphones", "price": 1200},
    {"name": "Cover", "price": 300}
]

print(products)
final_result = 0
items_buy = int(input("How many items do you want to buy : "))

def calulate(whichitem,quatity):
        if whichitem.lower() == "charger":
            return 800*quatity
        elif whichitem.lower() == 'earphone':
            return 1200*quatity
        elif whichitem.lower() == 'cover':
            return 300*quatity
        else:
            return "Please enter available Items"

for i in range (0,items_buy):
    which_items = input("Which Item you want to buy : ")
    quantity = int(input("Quantity of Items : "))
    result = calulate(which_items,quantity)
    final_result += result
    
print(final_result)