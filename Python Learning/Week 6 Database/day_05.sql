-- CTEs (with clause)

WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employee
    GROUP BY department
)
SELECT *
FROM dept_avg
WHERE avg_salary > 50000;


WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employee
    GROUP BY department
)
SELECT e.name, e.salary, e.department
FROM employee e
JOIN dept_avg d
ON e.department = d.department
WHERE e.salary > d.avg_salary;

WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employee
    GROUP BY department
)

SELECT e.name, e.salary, e.department
FROM employee e 
JOIN dept_avg d 
ON e.department = d.department
WHERE e.salary < d.avg_salary

with dept_count AS (
    SELECT department, COUNT(id) AS count_emp
    FROM employee
    GROUP BY department
)

SELECT department
FROM dept_count
WHERE count_emp > 2