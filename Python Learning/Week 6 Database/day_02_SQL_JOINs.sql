CREATE TABLE department (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);

CREATE TABLE employee (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,
    salary INTEGER,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

INSERT INTO department VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

INSERT INTO employee VALUES
(1, 'Ali', 1, 50000),
(2, 'Sara', 2, 45000),
(3, 'Umer', 1, 60000),
(4, 'Hina', 3, 55000),
(5, 'Bilal', 1, 48000);

SELECT e.name, d.dept_name, e.salary
FROM employee e
INNER JOIN department d
ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM department d
LEFT JOIN employee e
ON e.dept_id = d.dept_id;

SELECT d.dept_name, AVG(e.salary)
FROM employee e
JOIN department d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
