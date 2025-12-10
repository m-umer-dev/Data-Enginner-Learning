#Program 01

try:
    num1 = int(input("Enter 1st Number : "))
    num2 = int(input("Enter 2nd Number : "))
    num3 = int(input("Enter 3rd Number : "))

    print(f"Divide {num1/num2/num3}")

except ZeroDivisionError:
    print("Number Should not be divide by zero")

except ValueError:
    print("All Number Must be integers")

#Program 02

try:
    f = open ('lines.txt','r')
    file_data = f.read()
except FileNotFoundError:
    print("File Not Found")
else:
    print(f"Data Read Successfully : {file_data}")
finally:
    print("This will run everytime")

#Program 03

try:
    age = int(input("Enter Age : "))
    if age < 0:
        raise ValueError("Not Eligible")
    else:
        print("Eligible")
except ValueError as e:
    print(e)


#Program 04

while True:
    try:
        num = float(input("Enter Number : "))
        print(f"Valid float received: {num}")
        break
    except ValueError:
        print("Number Must be Float")