#Program 01

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        return f"Name : {self.name} , Salary : {self.salary}"
    
d1 = Employee("Data Engineer",30000)
d2 = Employee("Python",10000)
print(d1.show_info())
print(d2.show_info())