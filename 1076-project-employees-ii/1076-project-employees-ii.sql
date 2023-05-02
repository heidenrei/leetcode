# Write your MySQL query statement below
SELECT project_id 
FROM (
  SELECT project_id, COUNT(project_id),
  RANK() OVER(ORDER BY COUNT(project_id) DESC) as cnt
  FROM Project
  GROUP BY project_id
) t
WHERE t.cnt = 1;