SELECT department, AVG(salary)
FROM employee
GROUP BY department > (
    SELECT department, AVG(salary)
    FROM employee
)