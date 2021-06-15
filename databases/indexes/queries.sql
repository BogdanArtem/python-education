SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

begin;
savepoint S1;

/* QUERY1: Let's assume that we often perform name, surname search */
explain analyze
select *
from potential_customers pc
where name = 'Jenna' and surname = 'Ana';
-- Query planner performs seq scan with cost of 261 
-- Planning Time 0.286ms, Exec Time 4.502ms

create index name_surname
on potential_customers (name, surname);

explain analyze
select *
from potential_customers pc
where name = 'Jenna' and surname = 'Ana';
-- Query planner performs index scan with cost of 8.3 (x31)
-- Planning Time 0.956ms
-- Execution Time 0.707ms
-- PS Index boosted actual speed by x6

rollback to savepoint S1;


savepoint S2;

/* QUERY2: Let's assume that we often check orders with status 1 */
explain analyze
select *
from orders o
where o.order_status_order_status_id = 1
-- Query planner performs seq scan with cost of 56.75
-- Planning Time 0.078ms
-- Execution Time 9.206ms

create index unfinished_orders
on orders (order_status_order_status_id)
where order_status_order_status_id = 1

explain analyze
select *
from orders o
where o.order_status_order_status_id = 1
-- Query planner performs seq scan with cost of 51.82
-- Planning Time 0.478ms
-- Execution Time 10.029ms
-- PS No obvious speed increase, maybe due to the small table size

rollback to savepoint S2;


savepoint S3

/* QUERY3: Let's assume that we often check products by title */
explain analyse 
select *
from products p
where product_title = 'Product 1000';
-- Query planner performs seq scan with cost of 147
-- Planning Time 0.082ms
-- Execution Time 0.841ms

create index 
on products (product_title);

explain analyse 
select *
from products p
where product_title = 'Product 1000';
-- Query planner performs index scan with cost of 8.30
-- Planning Time 1.275ms
-- Execution Time 0.254ms
-- PS Index boosted actual speed by x3.3


rollback to savepoint S3;
rollback;

commit;
