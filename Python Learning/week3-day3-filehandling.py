#Program 01

import os
file_name  = input("Enter File Name : ")
if os.path.exists(file_name):
    with open (file_name,'r') as f:
        print(f.read())
else:
    print("File isn't exist")
    