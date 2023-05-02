# Write your MySQL query statement below
WITH score_count AS (
    SELECT
      (SELECT COUNT(*) FROM NewYork WHERE score >= 90) as NY_score,
      (SELECT COUNT(*) FROM California WHERE score >= 90) as CA_score
)

SELECT 
    CASE 
    WHEN NY_score > CA_score THEN "New York University"
    WHEN NY_score < CA_score THEN "California University"
    ELSE "No Winner"
    END as winner
FROM score_count;