# Write your MySQL query statement below
select distinct a.buyer_id 
from sales a
join product b on a.product_id = b.product_id
where b.product_name like 'S8' 
and  a.buyer_id not in (select buyer_id from 
                            product a join sales b on a.product_id = b.product_id 
                            where a.product_name like 'iPhone');