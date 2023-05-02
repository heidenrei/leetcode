# Write your MySQL query statement below
Select activity_date as 'day',
count(distinct user_id) as 'active_users'
from Activity
where activity_date > DATE_SUB("2019-07-27", INTERVAL 30 day) AND activity_date <= '2019-07-27'
GROUP BY activity_date
HAVING count(user_id) > 0