CREATE TABLE employee {
    id INTEGER PRIMARY KEY,
    name Text,
    department Text,
    salary INTEGER
}

INSERT INTO employee (name,department,salary) VALUES
('Ali', 'IT', 50000),
('Sara', 'HR', 45000),
('Umer', 'IT', 60000),
('Hina', 'Finance', 55000),
('Bilal', 'IT', 48000);

SELECT * FROM employee

SELECT * FROM employee WHERE department = "IT"

SELECT name, salary FROM employee WHERE salary >= 50000

SELECT department, AVG(salary) FROM employee GROUP BY department;