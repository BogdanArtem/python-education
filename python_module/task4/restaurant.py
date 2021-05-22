""" OOP representation of a restaurant"""

from abc import ABC
import random


class Person(ABC):
    """Abstract class of a person"""
    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._last_name = last_name

    @property
    def fname(self):
        """Get person's first name"""
        return self._first_name

    @property
    def lname(self):
        """Get person's last name"""
        return self._last_name


class Meal:
    """Meal that is used in menu"""
    def __init__(self, name: str, price: float, cooking_time: int):
        self._name = name
        self._price = price
        self._is_ready = False
        self._cooking_time = cooking_time

    def __repr__(self):
        """String representation of meal"""
        return self.name

    @property
    def name(self):
        """Get meal's name"""
        return self._name

    @property
    def price(self):
        """Get meals price"""
        return self._price

    @property
    def cooking_time(self):
        """Get meal's cooking time"""
        return self._cooking_time

    @property
    def is_ready(self):
        """Get meal's state"""
        return self._is_ready


class Order:
    """Class that represents orders in restaurant"""
    def __init__(self, meals: Meal) -> None:
        self._order_id = random.randint(0,10_000)
        self._meals = meals
        self._cust_id = None
        self._is_prepared = False
        self._is_served = False
        self._is_paid = False

    def __repr__(self):
        return f"<Order:[order_id: {self.order_id}, \
meals: {self.meals}, cust_id: {self.cust_id}, \
is_prepared: {self.is_prepared}], is_served: {self.is_served}, \
is_paid: {self.is_paid}"

    @property
    def order_id(self):
        """Get order id"""
        return self._order_id

    @property
    def meals(self):
        """Get list of ordered meals"""
        return self._meals

    @property
    def cust_id(self):
        """Get customer id"""
        return self._cust_id

    @cust_id.setter
    def cust_id(self, value):
        """Set customer id"""
        self._cust_id = value

    @property
    def is_prepared(self):
        """Get order's state"""
        return self._is_prepared

    @is_prepared.setter
    def is_prepared(self, value: bool):
        """Make order prepared"""
        self._is_prepared = value

    @property
    def is_served(self):
        """Get bool if order is served"""
        return self._is_served

    @is_served.setter
    def is_served(self, value: bool):
        """Set the state of order's serving"""
        self._is_served = value

    @property
    def is_paid(self):
        """Get the state of order's payment"""
        return self._is_paid

    @is_paid.setter
    def is_paid(self, value: bool):
        """Set the state of order's payment"""
        self._is_paid = value

    @property
    def cooking_time(self):
        """Get order's cooking time"""
        return max((time.cooking_time() for time in self.meals))


class OnlineOrder(Order):
    """Online order from customer account"""
    def __init__(self, meals: Meal, addr: str) -> None:
        super().__init__(meals)
        self._addr = addr
        self._is_delivered = False
        self._is_packed = False

    @property
    def addr(self):
        """Get online order delivery address"""
        return self._addr

    @property
    def is_delivered(self):
        """Get the order's state of delivery """
        return self._is_delivered

    @is_delivered.setter
    def is_delivered(self, value: bool):
        """Set the state of order's delivery"""
        self._is_delivered = value

    @property
    def is_packed(self):
        """Set the state of order's packaging"""
        return self._is_packed

    @is_packed.setter
    def is_packed(self, value: bool):
        """Set the state of order's delivery"""
        self._is_packed = value


class Employee(Person):
    """Abstract class of an Employee"""
    def __init__(self, fname: str, lname: str) -> None:
        super().__init__(fname, lname)
        self._employee_id = random.randint(0, 10_000)
        self._salary = 0

    def change_salary(self, amount: int) -> None:
        """Add or subtract amount of money from salary"""
        self._salary += amount

    @property
    def salary(self):
        """Get employee's salary"""
        return self._salary


class DeliveryBoy(Employee):
    """Employee that delivers products"""

    @staticmethod
    def pack(order: OnlineOrder):
        """Pack order"""
        order.pack()
        return order

    @staticmethod
    def deliver(order: OnlineOrder):
        """Deliver order"""
        order.deliver()
        return order


class Waiter(Employee):
    """Employee that serves food"""

    @staticmethod
    def serve(order: Order):
        """Serve order"""
        order.is_served = True


class Chief(Employee):
    """ Employee that cooks food"""

    @staticmethod
    def cook(order: Order) -> None:
        """Cook order"""
        order.is_prepared = True


class Menu:
    """Menu for a restaurant which consists of meals"""
    def __init__(self, meals:list) -> None:
        self._meals = meals

    @property
    def meals(self):
        """Get meals from menu"""
        return self._meals

    def get_item(self, name: str) -> Meal:
        """Find meal in menu by name"""
        return [meal for meal in self.meals if meal.get_name() == name][0]

    def cost_less_than(self, amount: float) -> list:
        """Find meals that cost less than amount"""
        return [meal for meal in self.meals if meal.get_price() < amount]

    def cook_less_than(self, time_m: int) -> list:
        """Find meals that take less than time_m minutes"""
        return [meal for meal in self.meals if meal.get_time() < time_m]

    def add_meal(self, meal: Meal) -> None:
        """Add meal to menu"""
        self.meals.append(meal)

    def remove_meal(self, name: str) -> None:
        """Remove meal in menu by name"""
        self.meals = [meal for meal in self.meals if meal.get_name() != name]


class CreditCard:
    """Credit card used in Account"""
    def __init__(self, card_num: int, holder: str) -> None:
        self._card_num = card_num
        self._holder = holder
        self._ballance = 0

    @property
    def card_num(self):
        """Get credit card number"""
        return self._card_num

    @property
    def holder(self):
        """Get credit card holder"""
        return self._holder

    @property
    def ballance(self):
        """Get credit card ballance"""
        return self._ballance

    @ballance.setter
    def ballance(self, value):
        """Change credit card ballance"""
        self._ballance = value

    def charge(self, amount:float) -> None:
        """Charge fixed amount of money from credit card"""
        self.ballance -= amount

    def top_up(self, amount:float) -> None:
        """Top up credit card with fixed amount of money"""
        self.ballance += amount


class Account:
    """User account to make online orders"""
    def __init__(self, login: str, password: str) -> None:
        self._account_id = random.randint(0,10_000)
        self._ph_num = None
        self._addr = None
        self._all_orders = []
        self._cards = []
        self._password = hash(password)
        self._login = login

    def add_cc(self, card: CreditCard) -> None:
        """Add credit card to user account"""
        self.cards.append(card)

    @property
    def account_id(self):
        """Get account id"""
        return self._account_id

    @property
    def ph_num(self):
        """Get account phone number"""
        return self._ph_num

    @property
    def addr(self):
        """Get address of account"""
        return self._addr

    @property
    def all_orders(self):
        """Get all orders for account"""
        return self._all_orders

    @property
    def cards(self):
        """Get all cards for account"""
        return self._cards

    @property
    def password(self):
        """Get account's hash of password"""
        return self._password

    @property
    def login(self):
        """Get account's login"""
        return self._login


class Customer(Person):
    """Visitor of a restaurant"""
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self._cust_id = random.randint(0,10_000)
        self._accounts = []

    @property
    def cust_id(self):
        """Get customer id"""
        return self._cust_id

    def make_order(self, a_menu: Menu, meals_num=1) -> Order:
        """Make order of random meals form menu"""
        order = Order(random.choices(a_menu.meals, k=meals_num))
        order.cust_id = self.cust_id
        return order

    @staticmethod
    def pay(order: Order) -> None:
        """Pay for order"""
        order.is_paid = True


class Table:
    """Restaurant's table to place customers"""
    def __init__(self, capacity: int) -> None:
        self._table_id = random.randint(0,10_000)
        self._capacity = capacity
        self._customers = []

    @property
    def capacity(self) -> int:
        """Get table's capacity"""
        return self._capacity

    @property
    def customers(self) -> list:
        """Get list of customers at the table"""
        return self._customers

    @property
    def table_id(self) -> int:
        """Get table's id"""
        return self._table_id

    def add_customer(self, cust: Customer) -> None:
        """Add customer to the table"""
        if self._capacity > len(self._customers):
            self._customers.append(cust)
        else:
            raise AttributeError("The table is full")

    def remove_customer(self, name):
        """Remove customer from the table"""
        self._customers = [cust for cust in self.customers if cust.name != name]


class Restaurant:
    """Representation of a restaurant"""
    def __init__(self, a_menu: Menu) -> None:
        self._menu = a_menu
        self._staff = []
        self._tables = []
        self._sales = []
        self._accounts = []

    @property
    def menu(self):
        """Get restaurant's menu"""
        return self._menu

    @property
    def staff(self):
        """Get restaurant's staff"""
        return self._staff

    @property
    def tables(self):
        """Get restaurant's tables """
        return self._tables

    @property
    def sales(self):
        """Get all sales"""
        return self._sales

    @property
    def accounts(self):
        """Get all accounts"""
        return self._accounts

    @property
    def gross_revenue(self) -> float:
        """Get all the money from paid orders"""
        return sum((order.get_total for order in self.sales if order.paid is True))

    @property
    def total_space(self) -> int:
        """Get total space of a restaurant"""
        return sum((table.get_space() for table in self.tables))

    @property
    def free_space(self) -> int:
        """Get free space of a restaurant"""
        return self.total_space - self.total_guests

    @property
    def total_guests(self) -> int:
        """Get number of guests of a restaurant"""
        return len((table.get_customers() for table in self.tables))

    def add_staff(self, cust: Employee) -> None:
        """Add employee to a restaurant"""
        self.accounts.append(cust)

    def remove_staff(self, empl_id: int) -> None:
        """Fire employee by his id"""
        self.staff = [empl for empl in self.staff if empl.employee_id != empl_id]

    def add_account(self, acc: Account) -> None:
        """Add user's account"""
        self.accounts.append(acc)

    def remove_account(self, acc_id: int) -> None:
        """Remove user's account"""
        self.accounts = [acc for acc in self.accounts if acc.account_id != acc_id]

    def add_sale(self, order: Order) -> None:
        """Add paid order"""
        self.sales.append(order)

    def add_table(self, table: Table) -> None:
        """Add a table to restaurant"""
        self.tables.append(table)

    def remove_table(self, tab_id: int) -> None:
        """Remove table from restaurant by table id"""
        self.tables = [table for table in self.tables if table.account_id != tab_id]


if __name__ == "__main__":
    # Create meals
    fired_chicken = Meal('Fried chicken', price=150, cooking_time=30)
    soup = Meal('French creame soup', price=50, cooking_time=50)
    potato = Meal('Baked potato', price=20, cooking_time=20)

    # Create menu
    menu = Menu([fired_chicken, soup, potato])

    # Create restaurant
    restaurant = Restaurant(menu)

    # Add some furniture to the restaurant
    table1 = Table(4)
    table2 = Table(2)
    table3 = Table(6)

    restaurant.add_table(table1)
    restaurant.add_table(table2)
    restaurant.add_table(table3)

    # Add employees to the restaurant
    delivery = DeliveryBoy("Mike", "Williams")
    chief = Chief("Emanuel", "Chirac")
    waiter = Waiter("Elisabeth", "Nickolson")
    restaurant.add_staff(delivery)
    restaurant.add_staff(chief)
    restaurant.add_staff(waiter)

    # Add some customers
    customer1 = Customer('John', 'Black')
    customer2 = Customer('Sam', 'Smith')
    customer3 = Customer('Nick', 'Manson')

    table1.add_customer(customer1)
    table1.add_customer(customer2)
    table1.add_customer(customer3)

    # Make orders
    order1 = customer1.make_order(menu, meals_num=2)
    order2 = customer2.make_order(menu)

    print("ORDERS CREATED...")
    print(order1)
    print(order2)

    # Cook orders
    chief.cook(order1)
    chief.cook(order2)

    # Serve orders
    waiter.serve(order1)
    waiter.serve(order2)

    # Pay for orders
    customer1.pay(order1)
    customer2.pay(order2)

    # Add it as a sale
    restaurant.add_sale(order1)
    restaurant.add_sale(order2)


    print("FINAL...")
    print(order1)
    print(order2)
