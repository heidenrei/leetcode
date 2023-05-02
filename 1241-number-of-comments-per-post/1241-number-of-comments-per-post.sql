# Write your MySQL query statement below
with posts as
(
select 
    distinct sub_id
from Submissions
where parent_id is null
)

select 
p.sub_id as post_id,
count(distinct s.sub_id) as number_of_comments
from Submissions as s
right join posts as p on s.parent_id=p.sub_id
group by p.sub_id