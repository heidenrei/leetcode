# Write your MySQL query statement below
select e.reports_to as 'employee_id', 
        (select distinct name from employees where employee_id = e.reports_to) as name, 
        count(*) as reports_count,
        round(avg(e.age)) as average_age
from employees e
where e.reports_to is not null
group by e.reports_to
order by employee_id
;