CREATE TABLE employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employee VALUES
(1,'Ali', 'IT', 50000),
(2,'Sara', 'HR', 45000),
(3,'Umer', 'IT', 60000),
(4,'Hina', 'Finance', 55000),
(5,'Bilal', 'IT', 48000);

SELECT name, department, salary,
ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employee;

SELECT name, department, salary,
RANK() OVER (ORDER BY salary DESC) AS rank_num
FROM employee;

SELECT name, department, salary,
DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employee;

SELECT *
FROM (
    SELECT 
        name,
        department,
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employee
) t
WHERE rnk = 1;

SELECT *
FROM (
    SELECT 
        name, 
        salary,
        department,
        RANK() over (PARTITION BY department ORDER BY salary DESC) AS rnk 
    FROM employee
) t
WHERE rnk <= 2;

SELECT *
FROM (
    SELECT 
        name, 
        salary,
        department,
        RANK() over (PARTITION BY department ORDER BY salary ASC) AS rnk 
    FROM employee
) t
WHERE rnk = 1;

SELECT 
    *,
    ROW_NUMBER() OVER (ORDER BY salary) AS row_num
FROM employee