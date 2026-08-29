# Write your MySQL query statement below
SELECT MAX(num) as num FROM (SELECT num from MyNumbers GROUP BY num HAVING COUNT(*) = 1) AS single_numbers;