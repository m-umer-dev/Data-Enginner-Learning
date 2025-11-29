#Program 01

word = input("Enter Word : ")
count = 0

for i in word:
    if i == 'a':
        count +=1
    elif i == 'e':
        count +=1
    elif i == 'i':
        count +=1
    elif i == 'o':
        count +=1
    elif i == 'u':
        count +=1

print(count)

#Program 02

products = {
    "mouse": 500,
    "keyboard": 1500,
    "usb": 300
}

print(products)
items_buy = int(input("how many different items want to buy? "))
final_amount = 0

def bill_calculation(items,quantity):
    items = items.lower()
    if items in products:
        return products[items]*quantity
    else:
        return None
    
for i in range(items_buy):
    items_name = input("item name? ")
    quantity = int(input("quantity? "))
    result = bill_calculation(items_name,quantity)

    if result == None:
        print("Items not found")
    else:
        final_amount += result

print(f"Total Bill Amount {final_amount}")

#Program 3
print('''At least 8 characters

Contains at least one number

Contains at least one uppercase letter

Contains at least one lowercase letter''')

password = input("Enter password & at least 8 characters : ")

hasupper = False
haslower = False
hasdigit = False

for i in password:
    if i.isupper():
        hasupper = True
    elif i.islower(): 
        haslower = True
    elif i.isdigit():
        hasdigit = True


if hasupper and haslower and hasdigit and password.__len__() >= 8:
    print("Stong Password")
else:
    print("Weak Password")