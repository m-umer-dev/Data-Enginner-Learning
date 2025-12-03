#Program 01

numbers = [2, 4, 4, 6, 2, 8, 8, 10]
new_set = set(numbers)
again_list = list(new_set)

print(again_list)

#Program 02

nums = [20, 7, 15, 9, 20]

max = nums[0]
min = nums[0]

for i in nums:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"max : {max}")
print(f"min : {min}")

#Program 03

students = {
    "Ali": 85,
    "Sara": 78,
    "Umer": 92,
    "Hina": 66
}

student_name = input("Enter Student Name : ")

if student_name in students:
    print(f"{student_name} scored {students[student_name]} marks.")
else: 
    print("Student Not Found")