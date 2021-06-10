/* Task 3.1*/
create table if not exists potential_customers(
	id integer primary key,
	email varchar(90),
	name varchar(50),
	surname varchar(90),
	second_name varchar(90),
	city varchar(90)
);

/* Select from potential customers and customers form city 17  */
select first_name, email 
from
	(select user_id, email, first_name, middle_name, last_name, city 
	from users 
	union
	select id, email, name, surname, second_name, city
	from potential_customers pc) as everyone
where city = 'city 17'

/* Task 3.2 */
/* Select emails of all users ordered by cities and name*/
select first_name, email
from users
	order by city, first_name

/* Task 3.3 */
/* Select names of groups grouped by count in descending order */
select category_title, count(*)
from categories c join products p
	on p.category_id = c.category_id
	group by category_title
	order by count(*) desc


/* Task 3.4 */
/* Select all products not in cart */
select product_title
from products
except(select product_title
	from products p join cart_product cp
	on p.product_id = cp.products_product_id );

/* Select not orderd products */
select product_title
from products p1
except(select distinct p2.product_title -- ordered products
	from products p2
		join cart_product cp
		on p2.product_id = cp.products_product_id
		join carts c
		on c.cart_id = cp.carts_cart_id
		join orders o
		on o.carts_cart_id = c.cart_id);

/* Select top 10 added to carts products */
select p.product_title, count(*) -- products in cart
from products p
	join cart_product cp
	on p.product_id = cp.products_product_id
	group by p.product_title
	order by count(*) desc
	limit 10;

/* Select top 10 ordered products */
-- PS it is assumes that all 5 order statuses are valid for this task
select p.product_title, count(o.order_id) as num_ord
from products p
	join cart_product cp
	on p.product_id = cp.products_product_id
	join carts c
	on c.cart_id = cp.carts_cart_id
	join orders o
	on o.carts_cart_id = c.cart_id
	group by p.product_title
  	order by num_ord desc
  	limit 10

  /* Select top 5 profitable users */
  select user_id, sum(o.total) as gross
  from users u
  	join carts c
  	on u.user_id = c.cart_id
	join orders o
	on o.carts_cart_id = c.cart_id
	-- Add filtering of canceled orders
	join order_status os
	on os.order_status_id = o.order_status_order_status_id
	where os.order_status_id != 4
	--
	group by user_id
	order by gross desc
	limit 5

  /* Select top 5 buying users */
  select user_id, count(o.order_id) buys
  from users u
  	join carts c
  	on u.user_id = c.cart_id
	join orders o
	on o.carts_cart_id = c.cart_id
	group by user_id
	-- PS each user has only one purchase

/* Select  top 5 canceling users */
  select user_id, sum(o.total) as gross
  from users u
  	join carts c
  	on u.user_id = c.cart_id
	join orders o
	on o.carts_cart_id = c.cart_id
	-- Filter only canceled users
	join order_status os
	on os.order_status_id = o.order_status_order_status_id
	where os.order_status_id = 4
	--
	group by user_id
	order by gross desc
	limit 5
