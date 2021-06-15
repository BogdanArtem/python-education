/* INSERT: Add cart with orders */
begin;
	savepoint S1;
	insert into carts values(9999, 40, 440, 500, now());
	insert into orders values(9999, 9999, 1, 60, 500, now(), now());

	savepoint S2;
	insert into carts values(99990, 30, 540, 600, now());
	insert into orders values(99990, 99990, 2, 60, 540, now(), now());
	-- undo inserts after S2
	rollback to savepoint S2;
commit;


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


/* UPDATE: Rise product price by 10% and update total, subtotal in Carts 
 * and total in Orders for unpaid orders (status 1 and 2) */
begin;
	-- Raise price of product by 10%
	update products
	set price = price * 1.1;

	
	-- Update total and subtotal in carts
	update carts as c
	set total = (
		select sum(price)
		from products p join cart_product cp
		on cp.products_product_id = p.product_id 
		join carts c1
		on c1.cart_id = cp.carts_cart_id
		where c.cart_id = c1.cart_id 
);
	update carts as c 
	set subtotal = total;
	

	-- Update orders using carts 
	update orders as o
	set total = (
		select sum(c.total)
		from orders o1 join carts c
		on o1.carts_cart_id = c.cart_id
		where o1.order_id = o.order_id 
	);
commit;
