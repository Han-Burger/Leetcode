# Write your MySQL query statement below
select Email from (
    (select Email, count(Email) from Person group by Email having count(Email) > 1) as p
);