# Write your MySQL query statement below
SELECT DISTINCT(c.title)
FROM Content as c
JOIN TVProgram as tv 
ON c.content_id = tv.content_id
WHERE (c.Kids_content = 'Y' AND c.content_type = 'Movies') AND 
tv.program_date BETWEEN "2020-06-01" AND "2020-06-30";