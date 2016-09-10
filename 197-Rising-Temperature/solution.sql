# Write your MySQL query statement below
SELECT d1.Id as Id FROM
Weather as d1 INNER JOIN Weather as d2
WHERE DATEDIFF(d1.Date, d2.Date) = 1 AND d1.Temperature > d2.Temperature