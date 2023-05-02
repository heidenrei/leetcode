# Write your MySQL query statement below
SELECT Master.employee_id
FROM
    (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
    UNION
    SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
    AS Master
WHERE Master.name IS NULL OR Master.salary IS NULL
ORDER BY employee_id ASC