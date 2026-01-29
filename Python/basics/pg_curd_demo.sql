
-- Grant roll to user to create database
SELECT rolcreatedb 
FROM pg_roles 
WHERE rolname = 'postgres';


-- Create DataBase
create database car_sales_db;

commit;

-- Creating a user 
create user car_sales_user with encrypted password 'totota_sales';

-- Grant full access to new user
alter database car_sales_db owner to car_sales_user;
commit;


-- Create a USERs Table
create table users (
	user_id SERIAL primary key,
	first_name varchar(50),
	last_name varchar(50)
	);

-- Insert data into users table
insert into users(first_name, last_name) 
values('Scott', 'Tiger'),
	('Donald', 'Trump'),
	('Durga', 'G')
;

select *
from users
;

-- update sir name for user_id
update users
set last_name = 'Gadiraju'
where user_id  = 3
;

-- Delete user_id 2 from the users table
delete from users
where user_id = 2
;

select *
from users
;