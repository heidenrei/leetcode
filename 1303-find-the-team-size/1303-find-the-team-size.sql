# Write your MySQL query statement below
with team_count as(
  select team_id, count(employee_id) as team_size
  from Employee 
  group by team_id
)

select e.employee_id, t.team_size
from Employee e join
team_count t using(team_id)