CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees (name, department, salary) VALUES
('Ali', 'IT', 50000),
('Sara', 'IT', 60000),
('Ahmed', 'HR', 45000),
('Fatima', 'HR', 55000),
('Usman', 'IT', 70000),
('Ameen', 'IT', 50000),
('Samreen', 'IT', 60000),
('Ashad', 'HR', 45000),
('Faraz', 'HR', 55000),
('Usama', 'IT', 70000);

SELECT 
    name, 
    department, 
    salary, 
    ROW_NUMBER() OVER(ORDER BY salary) AS id 
FROM employees

SELECT 
    name, 
    department, 
    salary, 
    ROW_NUMBER() OVER(ORDER BY salary) AS row_num, 
    RANK() OVER(ORDER BY salary) AS rank_num, 
    DENSE_RANK() OVER(ORDER BY salary) AS dense_rank_num
FROM employees;

-- 1️⃣ Find highest salary in each department
SELECT * FROM
    (SELECT 
        name, 
        department, 
        salary,
        ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS id
    FROM employees) AS high
WHERE id <= 1;

-- 2️⃣ Find 2nd highest salary in each department
SELECT * FROM
    (SELECT 
        name, 
        department, 
        salary,
        ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS id
    FROM employees) AS high
WHERE id = 2;

-- 3️⃣ Rank employees by salary (global)
SELECT 
    name, 
    department, 
    salary,
    RANK() OVER(ORDER BY salary DESC) AS id
FROM employees

-- 4️⃣ Rank employees by salary inside each department
SELECT 
    name, 
    department, 
    salary,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS id
FROM employees

-- 5️⃣ Calculate running total salary per department
SELECT 
    name,
    department,
    salary,
    SUM(salary) OVER(
        PARTITION BY department 
        ORDER BY salary 
    ) AS running_total
FROM employees;