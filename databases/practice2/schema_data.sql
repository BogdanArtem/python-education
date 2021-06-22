/* CREATE DATABASE SCHEMA */
begin;
create table if not exists cars (
	car_id integer primary key,
	model varchar(50) not null,
	plate varchar(20) not null,
	price integer not null
);

create table if not exists info (
	info_id integer primary key,
	state varchar(20) not null,
	address varchar(50) not null,
	phone varchar(20) not null
);

create table if not exists branches (
	branch_id serial primary key,
	info_id integer references info
);

create table if not exists customers (
	customer_id integer primary key,
	f_name varchar(50),
	l_name varchar(50),
	info_id integer references info
);

create table if not exists rentals (
	rent_id integer primary key,
	date date not null,
	period smallint not null,
	car_id integer references cars,
	branch_id serial references branches,
	customer_id integer references customers
);

commit;


/* FAKE DATA GENERATION */
begin;
-- Generate fake data for cars
insert into 
	cars
select 
	generate_series(0, 10000) as car_id,
	'car ' || generate_series(0, 10000) as model,
	-- generate 10 random characters 
	left(md5(random()::text), 10) as plate,
	-- generate prices between 1000 and 100
	random() * (1000-100+1) + 100 as price;

savepoint S1;

-- Generate fake data for info
insert into 
	info
select 
	generate_series(0, 1000000) as info_id,
	'state ' || floor(random() * (50)) as state,
	-- generate 10 random characters 
	left(md5(random()::text), 20) as address,
	floor(random() * 1000000000) as phone;

savepoint S2;

-- Generate fake data for branches
insert into
	branches(info_id)
select
	-- Unique nums from 0 to 100 for info_id referencing 
	num 
	from generate_series(0, 100) as s(num)
	order by random();

savepoint S3;

-- Generate fake data for customers
insert into
	customers
select
	-- subtract 100 to avoid info_id clashing
	generate_series(0, 1000000) as customer_id,
	'name ' || generate_series(0, 1000000) as f_name,
	'surname ' || generate_series(0, 1000000) as l_name,
	ceil(random() * 1000000) as info_id;
	
savepoint S4;

insert into
	rentals
select
	generate_series(0, 2000000) as rent_id,
	-- add 0-180 days to 2020-01-01
	'2020-01-01'::timestamp + (random() * (interval '180 days')) as dates,
	-- 1 to 30 days 
	ceil(random() * 30) as period,
	ceil(random() * 10000) as car_id,
	ceil(random() * 100) as branch_id,
	ceil(random() * 1000000) as customer_id;

commit;
