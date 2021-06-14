/* INSERT: Add cart with orders */
begin;
	savepoint S1;
	insert into carts values(9999, 40, 440, 500, now());
	insert into orders values(9999, 9999, 1, 60, 500, now(), now());

	savepoint S2;
	insert into carts values(99990, 30, 540, 600, now());
	insert into orders values(99990, 99990, 2, 60, 540, now(), now());
	rollback to savepoint S2;
commit;

-- select * from orders where order_id in (99990, 9999); -- id 99990 does not exist
-- select * from carts where cart_id in (99990, 9999); -- id 99990 does not exist


/* DELETE: Full delition of customer, including carts and orders */
begin;

	-- Delete orders for user_id
	delete from orders 
	where carts_cart_id in (
		-- In case if users has more than 1 cart
		select cart_id from carts 
		where users_user_id = 20
);

	-- Delete user by user_id 
	delete from users 
	where user_id = 20;

	-- Delete carts for user_id
	delete from carts 
	where users_user_id = 20;

commit;


/* UPDATE: Rise product price by 10% and update total in Orders and Carts for unpaid orders (status 1 and 2) */





