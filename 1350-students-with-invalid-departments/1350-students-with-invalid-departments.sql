# Write your MySQL query statement below
SELECT a.id, a.name
FROM Students a
LEFT JOIN Departments b
ON a.department_id = b.id
WHERE b.name IS NULL