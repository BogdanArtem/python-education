/* Create three views with one being a materialized view */


-- Find car models for each customer
create materialized view customer_car as
select c.f_name, c.l_name, cr.model 
from customers c join rentals r
	on c.customer_id = r.customer_id
	join cars cr
	on cr.car_id = r.car_id;

-- Find address for each customer
create view customer_address as 
select c.f_name, c.l_name, i.address
	from customers c join info i 
	on c.info_id = i.info_id

-- Find states for each car
create view car_state as 
select c.car_id, c.model, i.state
from cars c join rentals r
	on c.car_id = r.car_id
	join branches b
	on b.branch_id = r.branch_id
	join info i
	on i.info_id = b.info_id

-- select * from car_state limit 100;
-- select * from customer_address limit 100;
-- select * from customer_car limit 100;
