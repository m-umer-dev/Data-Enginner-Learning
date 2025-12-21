# Inheritance

#Program 01

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name} , Age : {self.age}")


class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks

    def show_info(self):
        print(f"Name : {self.name} , Age : {self.age} , Marks : {self.marks}")

    

p1 = Person('Ali',25)
s1 = Student('Taha',26,90)
p1.show_info()
s1.show_info()