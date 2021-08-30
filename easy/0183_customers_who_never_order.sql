select c.Name as Customers from Customers c
where c.id not in (select o.CustomerId from Orders o)