/* Write your T-SQL query statement below */
SELECT query_name, ROUND(SUM(CAST(rating as numeric(18,2)) / position) / COUNT(1), 2) AS quality,
        ROUND(CAST(SUM(IIF(rating <3, 1.00, 0.00)) / COUNT(query_name) as numeric(18,4)) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name
ORDER BY query_name;