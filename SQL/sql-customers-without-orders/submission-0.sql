-- Write your query below

-- for the customer names, we need to find the id for the customers and find the customer ids where the orders is 0

SELECT name FROM customers LEFT JOIN orders ON orders.customer_id = customers.id WHERE orders.id IS NULL;