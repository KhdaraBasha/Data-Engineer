
--	******************************************
--	CREATE SALES REP TABLE
--	******************************************
drop table if exists car_sales_db.public.tb_toyota_sales_rep;
create table car_sales_db.public.tb_toyota_sales_rep
	(
		rep_id	INTEGER PRIMARY KEY,
		first_name	VARCHAR(50),
		last_name	VARCHAR(50),
		email	VARCHAR(200) UNIQUE,
		phone_number	BIGINT,
		hire_date DATE,
		region	VARCHAR(20),
		status VARCHAR(20)
	)
;

GRANT SELECT, INSERT, UPDATE ON TABLE car_sales_db.public.tb_toyota_sales_rep to public;
--GRANT SELECT, INSERT, UPDATE ON TABLE car_sales_db.public.tb_toyota_sales_rep TO reporting_role;
