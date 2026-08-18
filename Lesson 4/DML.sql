--Part 1
--Insert new employees
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Adam', 'Sandler', 'Sales', 55000.00),
('Ryan', 'Gosling', 'Marketing', 62000.00);
--Employees from IT department
SELECT * FROM Employees; 
SELECT Firstname, Lastname
FROM Employees
WHERE Department = 'IT';
--Update Alice Smith salary
UPDATE Employees
SET Salary = 65000.00
WHERE Firstname = 'Alice' AND Lastname = 'Smith';
--Delete Eve Davis
DELETE FROM Employees
WHERE Firstname = 'Eve' AND Lastname = 'Davis';
--Select all
SELECT * FROM Employees
ORDER BY employeeid;

