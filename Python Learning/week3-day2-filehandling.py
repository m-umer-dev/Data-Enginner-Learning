#Program 01
import os
file_name = input("Enter File Name : ")

if os.path.exists(file_name):
    with open(file_name,'r') as f:
        print(f.read())
else :
    print("File does not exist")


#Program 02:

import os
if os.path.exists("note.txt"):
    with open("note.txt",'r') as f:
        print(f.readlines().__len__())
else :
    print("File does not exist")

#Program 03:

import os
if os.path.exists("abc.txt"):
    print("File already exists. Cannot overwrite.")
else:
    with open("abc.txt",'w') as f:
        f.write("hello")

#Program 04:

import os
if os.path.exists("lines.txt"):
    with open("lines.txt","r") as f1:
        with open("reversed.txt","w") as f2:
            f2.writelines(reversed(f1.readlines()))
else:
    print("File does not exist")