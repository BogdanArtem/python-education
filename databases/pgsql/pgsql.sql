
/* TASK1: Set shipping_total to zero if city matches */
create or replace function zero_shipping(target_city varchar) returns void as
$$
begin
	update orders 
	set shipping_total = 0
	where order_id in (
		select o.order_id 
		from users as u join carts as c
		on c.users_user_id = u.user_id
		join orders as o
		on o.carts_cart_id = c.cart_id
		where u.city = target_city
	);

	if not found then
		raise exception 'City "%" not found', target_city;
	end if;
end;
$$ language plpgsql;


/* Check */
begin;
select zero_shipping('city -150');

select o.shipping_total 
	from users as u join carts as c
	on c.users_user_id = u.user_id
	join orders as o
	on o.carts_cart_id = c.cart_id
	where u.city = 'city 150';

rollback;


/* TASK2: Write 2 stored procedures with loops,
 * transactions and conditional statements */


drop procedure ord_more_then

-- Show price of orders more that x
create or replace procedure ord_more_then(usd int)
language plpgsql
AS $$
DECLARE
    ord record;
begin
	raise notice 'Price limit is %', usd;
	for ord in
		select *
		from orders
	loop
		if ord.total > usd then
			raise notice 'Id is %, price is %', ord.order_id, ord.total;
		end if;
	end loop;
	raise notice '=========';
end;
$$;

call ord_more_then(3000);

-- Update total, subtotal in Carts
-- and total in Orders for unpaid orders (status 1 and 2)
create or replace procedure update_cart_total()
language plpgsql
as $$
declare
	_cart record;
	_prod record;
	_prod_sum int := 0;

begin
	-- For each cart
	for _cart in (
		select *
		from carts
	)
	loop
		_prod_sum = 0
		-- Find respective products
		for _prod in (
			select *
			from products p join cart_product cp
			on cp.products_product_id = p.product_id
			join carts c
			on c.cart_id = cp.carts_cart_id
			where c.cart_id = _cart.cart_id
	)
		-- Add up all product prices
		loop
			_prod_sum := _prod_sum + _prod.price;
		end loop;

		-- Update cart total
		update carts
		set total = _prod_sum;

		end loop;
end;
$$;

call update_total();

/* TASK3: Compare price of each product with average price of
 * its category using window function */

select c.category_title, p.product_title, p.price,
	avg(p.price) over(partition by c.category_title) as avg_price
	from products p
	join categories c
	using (category_id);

/* TASK 4: Write 2 triggers and trgger processor */

-- Add automatic time update to orders
create or replace function update_cart_time()
returns trigger
language plpgsql
as
$$
begin
	new.updated_at = now();
	return new;
end;
$$;

create trigger update_cart_time
	before update
	on orders
	for each row
	execute procedure update_cart_time();

-- Check
begin;
select * from orders where order_id = 2;

update orders
set total = total * 2 --0.5
where order_id = 2;

select * from orders where order_id = 2;
rollback;

-- Automatically add creation time upon creation of order
create or replace function add_creation_time()
returns trigger
language plpgsql
as
$$
begin
	new.created_at = now();
	return new;
end;
$$;

create trigger add_creation_time
	before insert
	on orders
	for each row
	execute procedure add_creation_time();

-- Check
begin;

insert into orders values (9999999, 1, 1, 835);
select * from orders where order_id = 9999999;

rollback;
