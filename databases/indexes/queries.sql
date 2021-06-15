SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

begin;
savepoint S1;

/* Let's assume that we often perform name, surname search */
explain analyze
select *
from potential_customers pc
where name = 'Jenna' and surname = 'Ana';
-- Query planner performs seq scan with cost of 261 
-- Planning Time 0.286ms, Exec Time 1.321ms

create index name_surname
on potential_customers (name, surname);

explain analyze
select *
from potential_customers pc
where name = 'Jenna' and surname = 'Ana';
-- Query planner performs index scan with cost of 8.3 (x31)
-- Planning Time 2.299ms
-- Execution Time 7.708ms
-- PS The increase of lookup time is probably due to the small size of the table

rollback to savepoint S1;


savepoint S2;

/* Let's assume that we often check orders with status 1 */
explain analyze
select *
from orders o
where o.order_status_order_status_id = 1
-- Query planner performs seq scan with cost of 56.75
-- Planning Time 0.146ms
-- Execution Time 7.259ms

create index unfinished_orders
on orders (order_status_order_status_id)
where order_status_order_status_id = 1

explain analyze
select *
from orders o
where o.order_status_order_status_id = 1
-- Query planner performs seq scan with cost of 51.82
-- Planning Time 0.348ms
-- Execution Time 6.401ms
-- PS actual speed increase in insignificant


rollback to savepoint S2;

commit;
