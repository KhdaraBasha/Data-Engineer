
-- Create Sales Table
create table customer_sales (
product_id int,
product_type nvarchar(128),
sales_price int,
salestime datetime
)

-- Insert Data into The Tables
insert into customer_Sales values(1,'mobile',10000,'2024-03-01 00:00:07.009')
insert into customer_Sales values(2,'freeze',40000,'2024-03-01 00:01:07.009')
insert into customer_Sales values(3,'mobile',40000,'2024-03-02 00:01:07.009')
insert into customer_Sales values(4,'tv',40000,'2024-03-02 00:01:07.009')
insert into customer_Sales values(5,'cooler',40000,'2024-03-03 00:01:07.009')
insert into customer_Sales values(6,'mobile',40000,'2024-03-04 00:01:07.009')
insert into customer_Sales values(7,'tv',40000,'2024-03-04 00:01:07.009')
insert into customer_Sales values(8,'cooler',40000,'2024-03-04 00:01:07.009')
insert into customer_Sales values(9,'mobile',40000,'2024-03-05 00:01:07.009')
insert into customer_Sales values(10,'tv',40000,'2024-03-05 00:01:07.009')
insert into customer_Sales values(11,'cooler',40000,'2024-03-05 00:01:07.009')

-- Create Procedure to Filter The Data
create procedure cust_sale
@startdate varchar(128),
@enddate varchar(128)
as begin
select * from customer_Sales
where salestime between @startdate and @enddate end

-- ADf Parameters
pipeline parameter
@trigger().outputs.windowstarttime
@trigger().outputs.windowEndtime