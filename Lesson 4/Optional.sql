--Part 6
SELECT ProjectName
FROM
	Projects
	INNER JOIN EmployeeProjects USING(ProjectID)
	INNER JOIN Employees USING(EmployeeID)
WHERE HoursWorked > 150 AND Firstname = 'Bob' AND Lastname = 'Johnson';
UPDATE Projects 
SET Budget = Budget * 1.1
WHERE ProjectID IN(
SELECT DISTINCT ProjectID
FROM employeeprojects
INNER JOIN Employees USING(EmployeeID)
WHERE Department = 'Senior IT'
);
UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;
BEGIN;
WITH new_employee AS (
	INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
	('Adam', 'Sandler', 'Sales', 55000.00)
	RETURNING EmployeeID
	)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT new_employee.EmployeeID, Projects.ProjectID, 80
FROM
Projects
INNER JOIN new_employee ON ProjectName = 'Website Redesign';
COMMIT;
SELECT * FROM employees 
SELECT * FROM employeeprojects
