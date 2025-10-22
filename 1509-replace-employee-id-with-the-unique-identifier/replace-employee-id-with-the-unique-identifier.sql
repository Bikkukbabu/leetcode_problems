# Write your MySQL query statement below
SELECT emp_un.unique_id, emp.name FROM Employees emp
left join EmployeeUNI emp_un
on emp.id = emp_un.id;
