-- 👉 Find employees who earn more than the average salary of their department.
WITH total AS (
    SELECT
        name,
        department,
        salary,
        AVG(salary) OVER(
            PARTITION BY department
        ) AS dept_avg
    FROM employees
)

SELECT *
FROM total
WHERE salary > dept_avg

-- 👉 Find employees whose salary is the 2nd highest in their department.
WITH emp_id AS (
    SELECT
        name,
        department,
        salary,
        DENSE_RANK() OVER(
            PARTITION BY department ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)

SELECT * 
FROM emp_id
WHERE salary_rank = 2;

-- 👉 Find employees whose salary is higher than the previous employee in the same department (based on salary order).
WITH emp_pre_sal AS (
    SELECT
        name,
        department,
        salary,
        LAG(salary) OVER(
            PARTITION BY department 
            ORDER BY salary
        ) AS previous_salary
    FROM employees
)

SELECT * 
FROM emp_pre_sal
WHERE salary > previous_salary

-- 👉 Find departments where salary strictly increases with each hire (based on hire_date).
WITH salary_check AS (
    SELECT
        department,
        salary,
        LAG(salary) OVER(
            PARTITION BY department
            ORDER BY hire_date
        ) AS previous_salary
    FROM employees
)

SELECT department
FROM salary_check
GROUP BY department
HAVING COUNT(
    CASE 
        WHEN salary <= previous_salary THEN 1
    END
) = 0;