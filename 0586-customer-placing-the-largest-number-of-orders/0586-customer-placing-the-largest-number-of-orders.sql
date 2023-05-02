select customer_number from Orders group by customer_number ORDER BY count(customer_number) DESC limit 1;
