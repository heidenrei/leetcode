# Write your MySQL query statement below
SELECT DISTINCT a.seat_id
FROM Cinema a, Cinema b
WHERE (a.seat_id+1=b.seat_id OR a.seat_id-1=b.seat_id) AND (a.free=1 AND b.free=1)