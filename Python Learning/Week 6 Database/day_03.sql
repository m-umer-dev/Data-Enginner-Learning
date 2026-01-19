SELECT AVG(salary) FROM employee;

SELECT name, salary
FROM employee
WHERE salary > (
    SELECT AVG(salary) FROM employee
);

SELECT name
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'IT'
);

SELECT name
FROM employee e
WHERE EXISTS (
    SELECT 1
    FROM department d
    WHERE d.dept_id = e.dept_id
);

SELECT name, salary
FROM employee e
WHERE salary > (
    SELECT AVG(salary)
    FROM employee
    WHERE dept_id = e.dept_id
);

CREATE INDEX idx_dept on employee(dept_id);

CREATE INDEX idx_salary on employee(salary);