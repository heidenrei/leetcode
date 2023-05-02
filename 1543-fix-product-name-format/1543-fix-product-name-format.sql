# Write your MySQL query statement below
select trim(lower(product_name)) product_name, date_format(sale_date,'%Y-%m') sale_date,
count(*) total
from sales 
group by 1,2
order by 1,2