# Write your MySQL query statement below
select distinct c.user_id 
from Confirmations c 
inner join Confirmations c1 
on c1.user_id=c.user_id
where c.time_stamp > c1.time_stamp and TIME_TO_SEC(TIMEDIFF(c.time_stamp,c1.time_stamp))<=86400
order by c1.user_id asc ;