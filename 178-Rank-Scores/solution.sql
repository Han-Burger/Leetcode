# Write your MySQL query statement below
select Score, (select count(distinct Score) from Scores where s.Score <= Score) Rank
from Scores s
order by Rank