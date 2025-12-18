#Program 01

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


p1 = Product("Mouse", 500)
p2 = Product("Keyboard", 1500)

p1.show_product()
p2.show_product()

print(p1.get_price())
