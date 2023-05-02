# Write your MySQL query statement below
WITH ordered AS (
    SELECT x - (Lag(x, 1) OVER(ORDER by x ASC)) as distance
    FROM Point
)

SELECT MIN(ABS(distance)) as shortest
FROM ordered