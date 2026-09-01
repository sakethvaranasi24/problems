# Write your MySQL query statement below
SELECT w.id FROM Weather w 
JOIN Weather k on datediff(w.recordDate , k.recordDate) = 1
WHERE w.temperature > k.temperature; 