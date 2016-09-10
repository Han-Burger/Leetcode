# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee, e.Salary from
Employee as e inner join Department as d
inner join
(select max(Salary) as maxSalary, DepartmentId
from Employee group by DepartmentId) as m
on e.DepartmentId = d.Id and d.Id = m.DepartmentId
where e.Salary = m.maxSalary