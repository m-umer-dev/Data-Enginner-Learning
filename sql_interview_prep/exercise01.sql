CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price DECIMAL(10,2)
);
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price INTEGER
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