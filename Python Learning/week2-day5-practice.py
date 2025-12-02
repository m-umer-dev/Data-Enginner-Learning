#Program 01

# numbers = [2, 4, 4, 6, 2, 8, 8, 10]
# new_set = set(numbers)
# again_list = list(new_set)

# print(again_list)

#Program 02

nums = [12, 7, 15, 9, 20]

max = 0
min = 0

for i in nums:
    for j in nums:
        if i > j:
            max = i
        elif i < j:
            min = i


print(f"max : {max}")
print(f"min : {min}")