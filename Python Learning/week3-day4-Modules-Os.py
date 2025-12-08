#Program 01

import math

num = int(input("Enter Number : "))
print(f"Square Root : {math.sqrt(num)}")
print(f"Factorial : {math.factorial(num)}")

#Program 02

import os

folder = "data_folder"
file_name = "sample.txt"
file_path = os.path.join(folder, file_name)

try:
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w") as f:
        f.write("Hello World")
    print(f"File created successfully: {file_path}")
except OSError as e:
    print("Failed to create file:", e)
