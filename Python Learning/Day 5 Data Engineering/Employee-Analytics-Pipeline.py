import csv

with open("company_employees.csv", newline="") as f:
    reader = csv.DictReader(f)
    employees = list(reader)

final_employees = []

for emp in employees:
    salary = int(emp["salary"])

    if salary >= 50000:
        if emp["department"] == "IT":
            salary = int(salary * 1.10)

        emp["salary"] = salary
        final_employees.append(emp)

with open("final_employees.csv", "w", newline="") as f:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(final_employees)
