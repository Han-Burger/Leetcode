# Write your MySQL query statement below
delete from Person where
Id not in (
    select Id from (
        select min(Id) as Id, Email from Person group by Email
    ) as p
);