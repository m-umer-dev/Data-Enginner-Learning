#Program 01

# name = input("Enter Name : ")

# strip = name.strip()
# lower = strip.lower()
# final = lower.capitalize()

# print(final)

#Program 02

# sentence = input("Enter Sentence & add bad word : ")
# print(sentence.replace("bad","good"))

#Program 03

products = {
    "charger": 800,
    "earphones": 1200,
    "cover": 300
}

print(products)
final_result = 0
items_buy = int(input("How many items do you want to buy : "))

def calculate(item, quantity):
    item = item.lower()
    if item in products:
        return products[item] * quantity
    else:
        return None

for i in range(items_buy):
    which_item = input("Which item you want to buy: ")
    quantity = int(input("Quantity: "))
    
    result = calculate(which_item, quantity)
    
    if result is None:
        print("❌ Item not found. Please select available items.")
    else:
        final_result += result

details = f"You bought {items_buy} items for a total price of {final_result}."
print(details)
