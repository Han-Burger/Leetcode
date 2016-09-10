# Write your MySQL query statement below
select Name as Customers from Customers
where Id not in (
#    select distinct c.Id from 
#    Customers as c inner join Orders as o
#    on c.Id = o.CustomerId
#    group by c.Id
    select distinct CustomerId from Orders
);