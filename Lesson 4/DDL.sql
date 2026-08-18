--Part 2
SELECT * FROM employees; --Select all
CREATE TABLE Departments --Create new table
(
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL, 
Location VARCHAR(50)
);
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100); --Add column for email
UPDATE Employees --Insert email
SET Email = 'smith543@example.com' WHERE Firstname = 'Alice' AND Lastname = 'Smith';
UPDATE Employees
SET Email = 'bob123jonson@example.com' WHERE Firstname = 'Bob' AND Lastname = 'Johnson';
UPDATE Employees
SET Email = 'charliebrown@example.com' WHERE Firstname = 'Charlie' AND Lastname = 'Brown';
UPDATE Employees
SET Email = 'dianaprince@example.com' WHERE Firstname = 'Diana' AND Lastname = 'Prince';
UPDATE Employees
SET Email = 'adamsand@example.com' WHERE Firstname = 'Adam' AND Lastname = 'Sandler';
UPDATE Employees
SET Email = 'ryangosling@example.com' WHERE Firstname = 'Ryan' AND Lastname = 'Gosling';
ALTER TABLE Employees ADD CONSTRAINT UQ_Email UNIQUE(email); --Unique email
ALTER TABLE Departments RENAME COLUMN LOCATION TO OfficeLocation;
SELECT * FROM employees;

