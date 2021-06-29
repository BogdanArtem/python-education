/* Write 3 procedures for insert, update and delete */


-- Add rental with date check
create or replace procedure add_rental(
	rent_id integer,
	date date,
	period integer,
	car_id integer,
	branch_id integer,
	customer_id integer
) language plpgsql
as $$
	begin 
		-- Check if date is in the past
		if date < now() then
			insert into rentals
			values (rent_id, "date", "period", car_id, branch_id);
		end if;
	end;
$$;

--begin;
--call add_rental(2000001, '2020-05-02'::date, 5, 50, 50, 50);
--rollback;


-- Delete short rentals
create or replace procedure delete_rentals_less_then(days integer)
language plpgsql
as $$
	begin
		if days > 0 then
			delete from rentals
			where "period" <= days;
		end if;
	end;
$$;

--begin;
--call delete_rentals_less_then(3);
--select * from rentals r where "period" <= 4;
--rollback;


-- Update model name for cars
create or replace procedure update_models(before varchar, after varchar)
language plpgsql
as $$
	begin
		-- Check that model does not exist
		if "before" not in (select model from cars) then 
			update cars
			set model = "after"
			where model = "before";
		end if;
	end;
$$;

--begin;
--select * from cars c limit 50;
--call update_models('car 0', 'mazda');
--select * from cars where model = 'mazda';
--call update_models('car 1', 'car 4');
--select * from cars where model = 'car 1';
--rollback;
