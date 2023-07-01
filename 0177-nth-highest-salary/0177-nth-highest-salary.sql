CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
      select distinct salary from employee e1 where (N-1) = (select count(distinct salary) from employee e2 where e1.salary < e2.salary) # order by salary desc
      
      
  );
END