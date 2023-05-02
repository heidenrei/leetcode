# Write your MySQL query statement below
SELECT S.user_id, 
SUM(P.price* S.quantity) AS spending
FROM Product P 
INNER JOIN Sales S
ON P.product_id = S.product_id
GROUP BY S.user_id
ORDER BY spending DESC, user_id ASC