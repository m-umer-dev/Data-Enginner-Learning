#Program 01

tuple = ('flash','weak hero 1','weak hero 2','study group','itaewon class')

print(tuple[0],tuple[-1],len(tuple))

#Program 02

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2),set1.intersection(set2),set1.difference(set2))

#Program 03

student = {
    "name": "Ali",
    "age": 20,
    "marks": {
        "math": 85,
        "english": 78,
        "science": 92
    }
}

print(student["name"])
print(student["marks"]["math"])
student["marks"]["student"] = 95
print(student)