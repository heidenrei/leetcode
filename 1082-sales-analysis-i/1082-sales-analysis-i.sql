# Write your MySQL query statement below
WITH sum_price AS(
SELECT seller_id,SUM(price) as price
FROM sales
GROUP BY seller_id)

SELECT seller_id
FROM sum_price
WHERE price = (SELECT MAX(price) FROM sum_price)