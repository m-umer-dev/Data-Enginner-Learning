-- SQL foundations reset

-- SUM Aggregate Function

SELECT 
    customer_id,
    SUM(quantity) AS total_orders
FROM orders
GROUP BY customer_id;

-- COUNT Aggregate Function

SELECT
    order_id,
    COUNT(product_id) AS total_order_product
FROM orders 
GROUP BY order_id;

-- AVG Aggregate Function

SELECT
    customer_id,
    AVG(quantity) AS avg_orders
FROM orders
GROUP BY customer_id;

-- MAX Aggregate Function

SELECT
    customer_id,
    MAX(quantity) AS max_order
FROM orders
GROUP BY customer_id;

-- Min Aggregate Function

SELECT
    customer_id,
    MIN(quantity) AS max_order
FROM orders
GROUP BY customer_id;