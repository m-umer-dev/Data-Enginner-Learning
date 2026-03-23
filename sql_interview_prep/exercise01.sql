CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customer VALUES
(1, 'Ali', 'Pakistan'),
(2, 'Sara', 'Pakistan'),
(3, 'John', 'USA'),
(4, 'Emma', 'UK'),
(5, 'Ahmed', 'UAE');

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 1200),
(2, 'Phone', 'Electronics', 800),
(3, 'Headphones', 'Electronics', 150),
(4, 'Chair', 'Furniture', 200),
(5, 'Desk', 'Furniture', 400);

INSERT INTO orders (order_id, customer_id, product_id, quantity) VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 1),
(5, 5, 5, 2),
(6, 1, 2, 1),
(7, 2, 3, 4),
(8, 3, 1, 1);

SELECT 
    c.country,
    SUM(o.quantity * p.price) AS total_sales
FROM orders o
JOIN customer c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id
GROUP BY c.country;

SELECT name, country FROM customer WHERE country = 'Pakistan'

SELECT c.name, p.product_name
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id

SELECT c.country, p.product_name
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE country = 'Pakistan';

SELECT c.country, o.quantity
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id;

SELECT c.country, SUM(o.quantity)
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY c.country;

SELECT c.name, p.product_name, o.quantity
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE c.country = 'Pakistan';

SELECT c.name, p.product_name, p.price
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE p.product_name = 'Laptop';

SELECT 
    c.name, 
    c.country, 
    p.product_name, 
    p.price * o.quantity AS total_price
FROM orders o
JOIN customer c 
    ON o.customer_id = c.customer_id
JOIN products p 
    ON o.product_id = p.product_id
WHERE c.country = 'Pakistan';

SELECT 
    c.country,
    SUM(p.price * o.quantity) AS total_revenue
FROM orders o
JOIN customer c 
    ON o.customer_id = c.customer_id
JOIN products p 
    ON o.product_id = p.product_id
GROUP BY c.country 
ORDER BY total_revenue DESC;

SELECT 
    c.name,
    SUM(p.price * o.quantity) AS total_spent,
    RANK() OVER (ORDER BY SUM(p.price * o.quantity) DESC) AS rank
FROM orders o
JOIN customer c 
    ON o.customer_id = c.customer_id
JOIN products p 
    ON o.product_id = p.product_id
GROUP BY c.name DESC;

SELECT 
    c.name,
    c.country,
    SUM(p.price * o.quantity) AS total_spent,
    RANK() OVER (ORDER BY SUM(p.price * o.quantity) DESC) AS rank
FROM orders o
JOIN customer c 
    ON o.customer_id = c.customer_id
JOIN products p 
    ON o.product_id = p.product_id
GROUP BY c.name DESC;