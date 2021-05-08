# Write your MySQL query statement below
DELETE L1 FROM Person L1 INNER JOIN Person L2 ON L1.Email = L2.Email and L1.ID > L2.ID;