# Write your MySQL query statement below
select w.name as warehouse_name, sum(width*length*height*units) as volume
from Warehouse w left join Products p
  on w.product_id = p.product_id 
group by w.name;