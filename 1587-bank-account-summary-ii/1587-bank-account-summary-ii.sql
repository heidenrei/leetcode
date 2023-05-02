/* Write your T-SQL query statement below */
select a.NAME , sum(amount) BALANCE
from Users a
left join
Transactions b
on a.account = b.account
group by a.name
having sum(amount) > 10000