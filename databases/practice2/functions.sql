/* Create 3 functions, one that returns table, one that uses loops, one that uses coursor */


-- Find sales for branch
create or replace function sales_by_branch(branch integer) returns 
	table (
		rent_id integer,
		price integer
	)
	language sql
	as $$
		select r.rent_id , c.price
		from branches b join rentals r
		on b.branch_id = r.branch_id
		join cars c
		on r.car_id = c.car_id
		where b.branch_id = branch;
	$$

-- select * from sales_by_branch(1);

	
-- Find first matching plate
create function first_matching_plate(p varchar) returns integer
	language plpgsql
	as $$
	declare
		car record;
	begin
		for car in (
			select plate, car_id from cars
		)
		loop
			if car.plate = p then
				return car.car_id;
			end if;
		end loop;
	end;
	$$;

-- select * from first_matching_plate('e4a52b9070');


-- Get list of car models in price range
create or replace function get_model_names(lower integer, upper integer)
   returns text as $$
declare
	 models text default '';
	 rec_model   record;
	 cur_models cursor(lower integer, upper integer)
		 for select model, price
		 from cars
		 where price between lower and upper;
begin
   open cur_models(lower, upper);
   models := 'Selected models are: ';

   loop
      fetch cur_models into rec_model;
      exit when not found;
      models := models || rec_model.model || ': ' || rec_model.price || '$, ';
   end loop;

   -- close the cursor
   close cur_models;
   return models;
end; $$
language plpgsql;

-- select * from get_model_names(100, 105);
