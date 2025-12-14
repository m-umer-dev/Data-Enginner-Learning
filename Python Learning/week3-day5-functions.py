#Program 01

def count_even (n):
    count = 0
    for i in n:
        if i % 2 == 0:
            count +=1

    return count

num_list = [1,2,3,4,5]
final_count = count_even(num_list)
print(final_count)

#Program 02

def bur_fun (items):
    print(items)
    items_name = input("Enter Item name : ")
    if items_name in items:
        return items[items_name]
    else:
        return "Not Found"



products = {
    "mouse": 500,
    "keyboard": 1500,
    "usb": 300
}

Price = bur_fun(products)
print(f"Price : {Price}")

#Program 03

def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

user_word = input("Enter Word : ")
print(is_palindrome(user_word))

#Program 04

def bur_fun (items):
    print(items)
    items_buy = int(input("How many items you want to buy : "))
    total_bill = 0
    for i in range(items_buy):
        items_name = input("Enter Item name you want to buy : ")
        if items_name in items:
            total_bill += items[items_name]
        else:
            print(f"{items_name} Not Found")

    return total_bill



products = {
    "mouse": 500,
    "keyboard": 1500,
    "usb": 300
}

bill = bur_fun(products)
print(f"Total Bill : {bill}")
