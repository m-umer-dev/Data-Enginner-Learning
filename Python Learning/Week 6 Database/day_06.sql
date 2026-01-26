-- Task 01

SELECT e.name, e.salary
FROM employee e
WHERE EXISTS (
    SELECT 1
    FROM employee x
    WHERE e.department = x.department
    AND e.salary < x.salary
)

-- Task 02

WITH depts_avg AS (
    SELECT department, AVG(salary) AS dept_avg
    FROM employee
    GROUP BY department
)
SELECT department
FROM depts_avg
WHERE dept_avg > (
    SELECT AVG(dept_avg)
    FROM depts_avg
);