# Write your MySQL query statement below
SELECT product.product_name, sales.year, sales.price FROM Sales sales
inner join Product product
on sales.product_id  = product.product_id