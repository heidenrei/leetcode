# Write your MySQL query statement below
select c.country_name, case when avg(w.weather_state) <= 15 then 'Cold'
                        when avg(w.weather_state) >= 25 then 'Hot'
                        else 'Warm'
                        end as weather_type
from countries c join weather w
on c.country_id = w.country_id
where year(w.day) = '2019' and month(w.day) = '11'
group by c.country_id;