SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

begin;
savepoint S1;

/* Let's assume that we perform often name, surname search */
explain
select *
from potential_customers pc
where name = 'Jenna' and surname = 'Ana';
-- Query planner performs seq scan with cost of 261

create index name_surname
on potential_customers (name, surname);

explain
select *
from potential_customers pc
where name = 'Jenna' and surname = 'Ana';
-- Query planner performs index scan with cost of 8.3 (x31)

rollback to savepoint S1;
commit;
