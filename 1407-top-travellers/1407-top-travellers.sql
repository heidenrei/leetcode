# Write your MySQL query statement below
select u.name ,sum(if(distance is null ,0,distance)) as travelled_distance 
from Users as u
left join Rides as r on u.id=r.user_id
group by user_id
order by travelled_distance desc,name