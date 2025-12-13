#Program 01

# def count_even (n):
#     count = 0
#     for i in n:
#         if i % 2 == 0:
#             count +=1

#     return count

# num_list = [1,2,3,4,5]
# final_count = count_even(num_list)
# print(final_count)

#Program 02

def bur_fun (items):
    print(items)
    items_buy = int(input("How many items you want to buy : "))
    items_name = input("Enter Item name you want to buy : ")

products = {
    "mouse": 500,
    "keyboard": 1500,
    "usb": 300
}

bur_fun(products)