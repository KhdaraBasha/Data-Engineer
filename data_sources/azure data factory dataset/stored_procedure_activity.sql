

select * from [dbo].[employee]

create procedure emp_delete @id int 
as 
begin 
delete from [dbo].[employee]
where emp_id = @id
end
;

exec [dbo].[emp_delete] @id = 1