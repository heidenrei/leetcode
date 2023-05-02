# Write your MySQL query statement below
SELECT product_id, "store1" as store, store1 as price
from Products
WHERE store1 != "null"
UNION ALL
SELECT product_id, "store2" as store, store2 as price
from Products
WHERE store2 != "null"
UNION ALL
SELECT product_id, "store3" as store, store3 as price
from Products
WHERE store3 != "null"