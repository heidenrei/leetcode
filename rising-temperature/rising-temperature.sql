# Write your MySQL query statement below
SELECT l1.ID AS ID
FROM Weather l1, Weather l2
WHERE DATEDIFF(l1.recordDate, l2.recordDate) = 1 and l1.Temperature > l2.Temperature;
