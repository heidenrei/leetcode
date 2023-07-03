# Write your MySQL query statement below
# select product_id, year as first_year, quantity, price
# from sales where (sale_id, year) in
# (select sale_id, min(year) as year
# from sales
#  group by product_id
# )

SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
SELECT product_id, MIN(year) as year
FROM Sales
GROUP BY product_id) ;