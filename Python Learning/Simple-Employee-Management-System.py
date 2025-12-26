class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def get_annual_bonus(self):
        return self.salary * 1.10
    
    def get_info(self):
        return f"{self.name} {self.salary}"


class DataEngineer(Employee):
    def __init__(self, name, salary, tools):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.tools = tools

    def get_annual_bonus(self):
        return self.salary * 1.20
    
    def get_info(self):
        return f"{self.name} {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.team_size = team_size

    def get_annual_bonus(self):
        return self.salary * 1.30
    
    def get_info(self):
        return f"{self.name} {self.salary}"


employees = [
    Employee('XYZ',5000),
    DataEngineer("XYZ",5000,'Data Engineer'),
    Manager("XYZ",5000,'3')
]

for emp in employees:
    print(emp.get_info())
    print("Bonus:", emp.get_annual_bonus())