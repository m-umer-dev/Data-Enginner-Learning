SELECT 
    c.country,
    SUM(p.price * o.quantity) AS total_spent
FROM orders o 
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.country ORDER BY total_spent DESC LIMIT 3;

SELECT
    c.name,
    COUNT(o.order_id) AS total_orders
FROM orders o 
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY c.name ORDER BY total_orders DESC;

SELECT *
FROM (
    SELECT
        c.name,
        COUNT(o.order_id) AS total_orders,
        RANK() OVER (ORDER BY COUNT(o.order_id) DESC) AS rnk
    FROM orders o 
    JOIN customer c ON o.customer_id = c.customer_id
    GROUP BY c.name
) t
WHERE rnk = 1;


SELECT
    c.name,
    AVG(o.order_id) AS avg_orders
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY c.name


SELECT
    c.name,
    SUM(p.price * o.quantity) / COUNT(o.order_id) AS total_value
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.name


SELECT * 
FROM
    (SELECT
        c.name,
        SUM(p.price * o.quantity) AS total_spent,
        COUNT(o.order_id) AS total_orders
    FROM orders o
    JOIN customer c ON o.customer_id = c.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.name) t

WHERE total_spent > 1000 AND total_orders > 1



SELECT
    c.name,
    SUM(p.price * o.quantity) AS customer_spent,
    (customer_spent / total_revenue) * 100 AS final_out
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.name