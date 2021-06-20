
/* Set shipping_total to zero if city matches */
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


