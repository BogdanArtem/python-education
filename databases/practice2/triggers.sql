/* Create 2 triggers, before and after alteration of data */

-- Delete rentals which reference car before deletion
create or replace function del_car_rentals() returns
	trigger
	language plpgsql
	as $$
		begin
			delete from rentals as r
			where r.car_id = old.car_id;
			return old;
		end;
	$$;
	end;
	
create trigger before_car_deletion
	before delete
	on cars
	for each row
	execute procedure del_car_rentals();

--begin;
--delete from cars where car_id = 5;
--select * from cars c where c.car_id = 5;
--select * from rentals r where r.car_id = 5;
--rollback;

-- Change date after changing rental duration
create or replace function change_date() returns
	trigger
	language plpgsql
	as $$
		begin
			update rentals as r
			set "date" = r."date" - (new."period" - r."period")
			where r."period" = old."period";
			return new;
		end;
	$$;
	end;
	
create trigger change_period
	after update
	on rentals
	for each row 
	execute procedure change_date();

--begin;
--select * from rentals r where r."period" = 1; -- e.g for 476866
--update rentals as r
--set "period" = 10
--where r.rent_id = 476866;
--select * from rentals r where r."period" = 10;
--rollback;
