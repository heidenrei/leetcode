CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT COALESCE(COUNT(user_id),0)  user_cnt FROM (SELECT user_id FROM Purchases
      WHERE time_stamp >= TIMESTAMP(startDate) AND time_stamp <= TIMESTAMP(endDate) AND amount >= minAmount
      GROUP BY user_id
      ) T1
      
      
  );
END