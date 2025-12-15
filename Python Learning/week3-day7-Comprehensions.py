#Program 01

num_list = [2, 4, 6, 8]

square = [n*2 for n in num_list]
print(square)

#Program 02

num_list = [1, 2, 3, 4, 5, 6, 7]

odd_nums = [n for n in num_list if n%2 != 0]
print(odd_nums)

#Program 03

name_list = ["ali", "umer", "sara"]

uppercase = [name.upper() for name in name_list]
print(uppercase)

#Program 04 

prices = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

price_with_tax = { item: price + price * 0.10 for item, price in prices.items() }

print(price_with_tax)