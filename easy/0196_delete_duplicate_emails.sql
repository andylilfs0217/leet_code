-- Delete rows from table 'p1'
DELETE p1 FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.id > p2.id