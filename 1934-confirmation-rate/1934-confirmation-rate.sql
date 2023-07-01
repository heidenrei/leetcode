# # Write your MySQL query statement below
# select confirmations.user_id, round((count(confirmations.user_id))/(max(1, count(signups.user_id))), 2) as confirmation_rate
# from signups join confirmations on signups.user_id=confirmations.user_id
select signups.user_id,
    ifnull(round(sum(case when action='confirmed' then 1 else 0 end)/
      (count(confirmations.user_id))
      , 2), 0) as confirmation_rate
from confirmations right join signups on confirmations.user_id=signups.user_id
group by signups.user_id