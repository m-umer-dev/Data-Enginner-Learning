import csv

with open("employees.csv",newline="") as f:
    reader = csv.DictReader(f)
    employees = list(reader)

for employee in employees:
    if employee["department"] == "IT":
        employee["salary"] = int(employee["salary"]) * 1.10

with open ("processed_employees.csv","w",newline="") as f:
    fieldnames = ["name","department","salary"]
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)