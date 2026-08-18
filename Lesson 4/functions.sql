--Part 5
CREATE FUNCTION CalculateAnnualBonus (
 employee_id INT, Salary NUMERIC) --Bonuses
 RETURNS NUMERIC
 LANGUAGE PlpgSQL
 AS $$
 BEGIN
 	RETURN salary * 0.10;		
 END;
 $$;
SELECT EmployeeID, CalculateAnnualBonus(EmployeeID, Salary)
FROM Employees;
CREATE OR REPLACE VIEW IT_Department_View AS --IT department
SELECT 
EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Department = 'Senior IT';
SELECT * FROM IT_Department_View;
