# Write your MySQL query statement below
SELECT q.query_name, 
ROUND(SUM(q.rating / q.position) / COUNT(query_name), 2) as quality,
ROUND(SUM(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END) * 100.00 / COUNT(q.rating), 2) as poor_query_percentage
FROM Queries q
GROUP by q.query_name;