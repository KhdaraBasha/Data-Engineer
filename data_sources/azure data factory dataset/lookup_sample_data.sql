
--------------------------------------------------------
-- Create EMPLOYEE TABLE
CREATE TABLE dbo.tb_employee (
	id int,
	name varchar(250),
	country varchar(250)
	)
;

-- INSERt DATA INTO EMPLOYEE TABLE
INSERT INTO dbo.tb_employee VALUES(1, 'basha', 'india')
INSERT INTO dbo.tb_employee VALUES(2, 'basha', 'usa')
INSERT INTO dbo.tb_employee VALUES(3, 'basha', 'india')
INSERT INTO dbo.tb_employee VALUES(4, 'basha', 'india')
INSERT INTO dbo.tb_employee VALUES(5, 'basha', 'usa')
INSERT INTO dbo.tb_employee VALUES(6, 'basha', 'india')
INSERT INTO dbo.tb_employee VALUES(7, 'basha', 'india')
INSERT INTO dbo.tb_employee VALUES(8, 'basha', 'india')
;

--------------------------------------------------------
-- CRETAE EMPLOYEE RESIGON TABLE
CREATE TABLE dbo.tb_employee_resign (
	id int
	)
;

-- INSERT DATA INTO EMPLOYEE RESIGON TABLE
INSERT INTO dbo.tb_employee_resign VALUES(1)
INSERT INTO dbo.tb_employee_resign VALUES(2)
;

---------------------------------------------------------
-- CREATE STORED PROCEDURE TO DELETE THE EMPLOYEE THOSE ARE RESIGNED
CREATE PROCEDURE dbo.st_proc_emp_delete @id int 
AS
BEGIN
DELETE FROM dbo.tb_employee 
WHERE id = @id
END
;

-- COMMAND FOR EXECUTE STORED PROCEDURE
EXEC dbo.st_proc_emp_delete @id = 1


