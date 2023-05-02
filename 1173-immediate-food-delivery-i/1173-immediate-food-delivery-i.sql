# Write your MySQL query statement below
with extraction as (
select delivery_id, order_date, customer_pref_delivery_date as pref
from Delivery d),
case_extract as(
    select e.delivery_id,
    case 
    when e.order_date = e.pref 
    then 'immediate'
    else 'scheduled' end as "grouping"
    from extraction e
),
group_immediate as(
    select c.delivery_id, c.grouping as groupingi
    from case_extract c
    where c.grouping = 'immediate'
), group_i_count as(
    select count(i.groupingi) as immediate_count
    from group_immediate i
), combo as(select i.*, (select count(s.delivery_id)
from extraction s) as total_count
from group_i_count i), divide as(
    select round((c.immediate_count/c.total_count)*100,2) as immediate_percentage
    from combo c
)
select * from divide;