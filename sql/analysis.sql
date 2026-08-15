-- Sales ETL Analytics

-- Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- Total sales
SELECT SUM(amount) AS total_sales
FROM sales;

-- Average order value
SELECT
    AVG(amount) AS average_order_value
FROM sales;

-- Sales by status
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(amount) AS total_sales
FROM sales
GROUP BY status
ORDER BY total_sales DESC;

-- Sales by category
SELECT
    category,
    COUNT(*) AS orders,
    SUM(amount) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;
