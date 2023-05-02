# Write your MySQL query statement below
SELECT seller_name from seller where seller_name NOT IN(
SELECT seller_name
FROM ORDERS join seller using(seller_id)
WHERE YEAR(sale_date)=2020
) order by seller_name