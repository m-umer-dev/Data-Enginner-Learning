# Program 01

sentence = input("Enter Sentence : ")

with open("note.txt",'a') as f:
    f.write(sentence)

#Program 02

with open("note.txt","r") as f:
    print(f.read())

#Program 03

n = int(input("How many lines do you want to write? "))
lines = []

for i in range(n):
    text = input("Please Type Text : ")
    lines.append(text +'\n')

with open("lines.txt",'w') as f:
    f.writelines(lines)