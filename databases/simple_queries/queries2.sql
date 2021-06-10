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
