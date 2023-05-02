# Write your MySQL query statement below
select b.player_id,b.device_id
from Activity b
where (b.player_id,b.event_date) in
(select a.player_id,min(a.event_date)
from Activity a
group by a.player_id)