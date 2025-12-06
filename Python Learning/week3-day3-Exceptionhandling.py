#Program 01

num1 = int(input("Enter Number One  : "))
num2 = int(input("Enter Number Two : "))

try:
    print(num1/num2)
except ZeroDivisionError:
    print("Cannot divide by zero")

#Program 02

import os

try:
    with open ('abc.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")

#Program 03

num = input("Enter Number : ")

try:
    num_check = int(num)
except ValueError:
    print("Invalid input! Enter a number")