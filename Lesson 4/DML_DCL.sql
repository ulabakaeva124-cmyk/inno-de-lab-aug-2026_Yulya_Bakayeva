--Part 4
UPDATE Employees --Update salary for HR department
SET Salary = Salary * 1.1
WHERE Department = 'HR';
UPDATE Employees --Create new department
SET Department = 'Senior IT'
WHERE Salary > 70000.00 AND Department = 'IT';
DELETE FROM Employees e --Delete emloyees without projects
WHERE NOT EXISTS (
	SELECT Employeeid
	FROM EmployeeProjects ep
	WHERE ep.Employeeid = e.Employeeid
	);
BEGIN; --Add a new project and its executors
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) VALUES
('Security System Update', 90000.00, '2026-08-14', '2026-10-26');
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked) VALUES
(2, 4, 100), --  Bob Johnson (ID 2) on Security System Update (ID 1)
(4, 4, 80); -- Diana Prince (ID 4) on Security System Update (ID 1)
COMMIT;	
SELECT * FROM employees
