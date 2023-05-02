# Write your MySQL query statement below
WITH total_requests AS (
SELECT 
    COUNT(DISTINCT sender_id, send_to_id) AS requests
FROM FriendRequest )
,
accepted_requests AS (
SELECT
   COUNT(DISTINCT requester_id, accepter_id) AS accepts
FROM RequestAccepted )


SELECT
    ROUND(COALESCE(accepts/requests, 0), 2) AS accept_rate
FROM total_requests, accepted_requests