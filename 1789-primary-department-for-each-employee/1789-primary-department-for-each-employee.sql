# Write your MySQL query statement below
SELECT emp_primary_dept.employee_id, emp_primary_dept.department_id
FROM
(
SELECT emp.employee_id, emp.department_id, emp.primary_flag, emp_dept_cnt.dept_cnt
FROM Employee emp
JOIN 
(
    SELECT employee_id, COUNT(DISTINCT department_id) AS dept_cnt
    FROM Employee 
    GROUP BY 1
) emp_dept_cnt
ON emp.employee_id = emp_dept_cnt.employee_id
) emp_primary_dept
WHERE emp_primary_dept.dept_cnt = 1 OR emp_primary_dept.primary_flag = 'Y'