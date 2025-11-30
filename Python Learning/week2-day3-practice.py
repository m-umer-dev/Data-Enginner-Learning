#Program 01

list = [2,5,8,11,14,17]
even_list = []

for i in list:
    if i%2 == 0:
        even_list.append(i)

    
print(even_list)

#Program 02

products = {
    "mouse": 500,
    "keyboard": 1500,
    "usb": 300,
    "monitor": 8000,
    "laptop": 75000
}

product_name = input("PLease enter product name : ")

if product_name in products:
    print(f"Price of {product_name} is Rs: {products[product_name]}")
else:
    print("Product Not found")

#Program 03 Frequency counter

sentence = input("Write Sentence : ")
dict = {}
dict = sentence.split()

dict_count = {}

for i in dict:
    if i in dict_count:
        dict_count[i] += 1
    else:
        dict_count[i] = 1

print(dict_count)