# Write your MySQL query statement below
# Write your MySQL query statement below
select st.student_id,st.student_name,sb.subject_name,COUNT(ex.subject_name) attended_exams 
from Students as st CROSS JOIN subjects as sb LEFT JOIN Examinations as ex 
on ex.student_id=st.student_id and ex.subject_name=sb.subject_name 
group by st.student_id ,sb.subject_name,st.student_name 
order by st.student_id ,sb.subject_name