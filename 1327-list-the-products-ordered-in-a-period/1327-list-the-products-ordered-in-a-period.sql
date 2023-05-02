# Write your MySQL query statement below
with validDate as (select product_name, unit from Products p join Orders o
on p.product_id = o.product_id
where o.order_date between '2020-02-01' and '2020-02-29')

select product_name, sum(unit) as unit from validDate
group by product_name 
having sum(unit) >= 100;