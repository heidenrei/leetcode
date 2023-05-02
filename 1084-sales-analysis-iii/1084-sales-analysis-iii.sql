# Write your MySQL query statement below
select p.product_id, p.product_name
from Product p
join Sales s using(product_id)
where product_id not in (select product_id
from Product p
left join Sales s using(product_id)
where month(sale_date) not in (1,2,3))
group by product_id