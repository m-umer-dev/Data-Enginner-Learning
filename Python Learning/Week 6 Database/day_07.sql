-- Bad SQL Query

SELECT * FROM employee WHERE salary = 50000;

-- Improve & Best Practice

SELECT name, salary FROM employee WHERE salary = 50000;

-- When would you NOT use an index?

-- Indexes are not useful for small tables or queries that return
-- many rows, because a full table scan is faster and the 
-- database may ignore the index.