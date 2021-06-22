/* Write 3 different querries and optimize them */

-- Plates of cars by customer name
explain analyse 
select cr.plate
from customers c join rentals r
	on c.customer_id = r.customer_id 
	join cars cr
	on cr.car_id = r.car_id 
	where c.f_name = 'name 43104'
-- Execution time: 37s

-- Index to search for plates
create index on customers(f_name);
create index on rentals(customer_id);
create index on rentals(car_id);

explain analyse 
select cr.plate
from customers c join rentals r
	on c.customer_id = r.customer_id 
	join cars cr
	on cr.car_id = r.car_id 
	where c.f_name = 'name 43104'
-- Execution time: 231ms


-- Find customer who uses phone 679203064
explain analyze
select c.f_name || ' ' || c.l_name as name
from customers c join info i
	on c.info_id = i.info_id
	where i.phone = '679203064';
-- Execution time: 20s

create index on info(phone);
create index on customers(info_id);

explain analyze
select c.f_name || ' ' || c.l_name as name
from customers c join info i
	on c.info_id = i.info_id
	where i.phone = '679203064';
-- Execution time: 0.464ms

-- Find customers who rented at branch 1
explain analyze
select c.f_name || ' ' || c.l_name as name
from customers c join rentals r 
	on c.customer_id = r.customer_id
	join branches b 
	on b.branch_id = r.branch_id 
	where b.branch_id = 1;
-- Execution time 25s

create index on rentals(branch_id);

explain analyze
select c.f_name || ' ' || c.l_name as name
from customers c join rentals r 
	on c.customer_id = r.customer_id
	join branches b 
	on b.branch_id = r.branch_id 
	where b.branch_id = 1;
-- Execution time 16s
