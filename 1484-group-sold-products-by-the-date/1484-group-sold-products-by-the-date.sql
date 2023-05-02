/* Write your T-SQL query statement below */
with CTE_Distinct_SellDate_Product as (
  select
  distinct
    sell_date
    ,product
  from
    Activities
)

select
  a.sell_date
  ,count(a.product) as num_sold
  ,STRING_AGG(a.product,',') WITHIN GROUP (ORDER BY a.product) as products
from
  CTE_Distinct_SellDate_Product a
group by  
  a.sell_date
order by
  a.sell_date