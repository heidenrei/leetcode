# Write your MySQL query statement below
SELECT employee_id,
case when employee_id%2 <>0 and name not like 'M%' then salary 
else 0
end as bonus FROM employees order by employee_id;