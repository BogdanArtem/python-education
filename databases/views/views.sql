begin;
savepoint S1;

/* Select all products */
create or replace view get_all_products as
select * 
	from products;
-- select * from get_all_products;

savepoint S2;

/* Select orders with respective status */
create or replace view orders_with_status as
select o.order_id, os.status_name 
	from orders o join order_status os
	on o.order_status_order_status_id = os.order_status_id;
-- select * from orders_with_status;

savepoint S3;

/* Select product name with respective category name */
create or replace view products_with_category as
select p.product_title, c.category_title 
	from products p join categories c 
	using (category_id);
-- select * from products_with_category;

savepoint S4;

/* Calculate price for each order status */
create materialized view category_sum as
select os.status_name , sum(p.price)
from order_status os join orders o 
	on os.order_status_id = o.order_status_order_status_id
	join carts c 
	on o.carts_cart_id = c.cart_id 
	join cart_product cp 
	on c.cart_id = cp.carts_cart_id
	join products p
	on p.product_id = cp.products_product_id
	group by os.status_name;
-- explain analyze select * from category_sum;

savepoint S5;

/* Drop all views */
drop view get_all_products;
drop view orders_with_status;
drop view products_with_category;
drop materialized view category_sum;

commit;
