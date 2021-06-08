CREATE TABLE IF NOT EXISTS Users(
	user_id integer PRIMARY KEY,
	email varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	middle_name varchar(255),
	is_staff smallint NOT NULL,
	country varchar(255) NOT NULL,
	city varchar(255) NOT NULL,
	address text NOT NULL
);

CREATE TABLE IF NOT EXISTS Order_status(
	order_status_id integer PRIMARY KEY,
	status_name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Categories(
	category_id integer PRIMARY KEY,
	category_title varchar(255) NOT NULL,
	category_description text NOT NULL
);

CREATE TABLE IF NOT EXISTS Carts(
	cart_id integer PRIMARY KEY,
	Users_user_id integer REFERENCES USERS ON DELETE CASCADE,
	subtotal decimal,
	total decimal,
	timestamp timestamp(2)
);

CREATE TABLE IF NOT EXISTS Orders(
	order_id integer PRIMARY KEY,
	Carts_cart_id integer REFERENCES Carts ON DELETE CASCADE ,
	Order_status_order_status_id integer REFERENCES Order_status ON DELETE RESTRICT,
	shipping_total decimal,
	total decimal,
	created_at timestamp(2),
	updated_at timestamp(2)
);

CREATE TABLE IF NOT EXISTS Products(
	product_id integer PRIMARY KEY,
	product_title varchar(255),
	product_description text,
	in_stock integer,
	price real,
	slug varchar(45),
	category_id integer REFERENCES Categories ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Cart_product(
	carts_cart_id integer REFERENCES Carts ON DELETE CASCADE,
	products_product_id integer REFERENCES Products ON DELETE CASCADE
);

COPY users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
FROM '/docker-entrypoint-initdb.d/users.csv'
DELIMITER ',';

COPY order_status(order_status_id, status_name)
FROM '/docker-entrypoint-initdb.d/order_statuses.csv'
DELIMITER ',';

COPY categories(category_id, category_title, category_description)
FROM '/docker-entrypoint-initdb.d/categories.csv'
DELIMITER ',';

COPY carts(cart_id, Users_user_id, subtotal, total, timestamp)
FROM '/docker-entrypoint-initdb.d/carts.csv'
DELIMITER ',';

COPY orders(order_id, Carts_cart_id, Order_status_order_status_id, shipping_total, total, created_at, updated_at)
FROM '/docker-entrypoint-initdb.d/orders.csv'
DELIMITER ',';

COPY products(product_id, product_title, product_description, in_stock, price, slug, category_id)
FROM '/docker-entrypoint-initdb.d/products.csv'
DELIMITER ',';

COPY cart_product(carts_cart_id, products_product_id)
FROM '/docker-entrypoint-initdb.d/cart_products.csv'
DELIMITER ',';