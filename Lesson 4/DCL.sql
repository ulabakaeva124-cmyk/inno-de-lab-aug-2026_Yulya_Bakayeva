--Part 3
CREATE USER hr_user WITH PASSWORD 'user12345'; --Create new connection
GRANT SELECT ON Employees TO hr_user;
GRANT INSERT, UPDATE ON Employees TO hr_user;
