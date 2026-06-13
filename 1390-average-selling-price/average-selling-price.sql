# Write your MySQL query statement below
SELECT p.product_id, 
CASE 
    WHEN SUM(us.units) is NULL THEN 0
    ELSE ROUND(SUM(us.units * p.price) / SUM(us.units), 2) 
 END AS average_price
FROM Prices p
LEFT JOIN UnitsSold us
ON p.product_id = us.product_id 
AND us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

