
-- CREATE EMPLOYEE TABLE
DROP TABLE IF EXISTS dbo.tb_employee;
CREATE TABLE dbo.tb_employee (
	employee_id int,
	FirstName varchar(150),
	salary int,
	location varchar(150)
	)
;

-- INSERT DATA INTO EMPLOYEE TABLE
INSERT INTO tb_employee VALUES(1, 'manish', 10000, 'india')
INSERT INTO tb_employee VALUES(2, 'neha', 5000, 'india')
INSERT INTO tb_employee VALUES(4, 'surya', 5000, 'uk')
;