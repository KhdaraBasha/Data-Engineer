
--	******************************************
--	CREATE TOYOTA SALES TABLE
--	******************************************
drop table if exists car_sales_db.public.tb_toyota_sales;
create table car_sales_db.public.tb_toyota_sales
	(
		sale_id	INTEGER primary key,
		sale_rep_id	INTEGER references tb_toyota_sales_rep(rep_id),
		sale_date	DATE,
		car_model	VARCHAR(50),
		sale_amount	numeric(10,2),
		commission_pct	numeric(5,2),
		sale_status VARCHAR(20)
	)
;

GRANT SELECT, INSERT, UPDATE ON TABLE car_sales_db.public.tb_toyota_sales to public;
--GRANT SELECT, INSERT, UPDATE ON TABLE car_sales_db.public.tb_toyota_sales TO reporting_role;