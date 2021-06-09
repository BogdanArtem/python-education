/* Task 2.1 */
/* Select all users */
select * from users;

/* Select all products */
select * from products;

/* Select all order status */
select * from order_status;

/* Task 2.2 */
/* Select paid and delivered orders */
select * from orders where order_status_order_status_id = 4;

/* Task 2.3 */
/* Select products with price range (80; 150] */
select * from products where price > 80 and price <= 150;

/* Select orders after 01.10.2020 (01 is not included) */
select * from orders where created_at > '2020-10-01';

/* Select orders created in the first half of 2020 (06-01 is not included) */
select * from orders where created_at between '2020-01-01' and '2020-06-01'

/* Select products of categories Category 7, Category 11, Category 18 */
select * from products where category_id in (7, 11, 18)

/* Select unfinished orders before 31.12.2020  */
select * from orders where order_status_order_status_id in (1, 2, 3) 
-- 1 - accepted; 2 - in progress; 3 - paid; 4 - finished; 5 - canceled
and created_at < '2020-12-31'; 

/* Select all carts without orders */
select cart_id from carts 
except
select distinct o.carts_cart_id from orders o 




