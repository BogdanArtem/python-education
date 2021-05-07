"""This module is used to implement OOP concepts in Python"""

from abc import ABC, abstractmethod
import random


class Transport(ABC):
    """Abstract class for transport"""

    def __init__(self, t_name, driver, capacity):
        """Transport should have name, driver and optionally some passangers"""
        self._driver = driver
        self.passangers = []
        self._t_name = t_name
        self.capacity = capacity

    def __repr__(self):
        return f"Transport[driver: {self.driver},\
transport: {self.t_name}, \
capacity: {self.capacity}, \
passangers: {self.passangers}]"

    def __hash__(self):
        return hash(self.t_name + str(self.capacity) + str(hash(self.driver)))

    def __eq__(self, other):
        """Defines behavior for the equality operator, ==."""
        return (self.driver == other.driver) and\
            (self.passangers == other.passangers) and\
            (self.t_name == other.t_name) and\
            (self.capacity == other.capacity)

    def __lt__(self, other):
        """Defines behavior for the less-than operator, <."""
        return self.capacity < other.capacity

    def __gt__(self, other):
        """Defines behavior for the greater-than operator, >."""
        return self.capacity > other.capacity

    def __le__(self, other):
        """Defines behavior for the less-than-or-equal-to operator, <=."""
        return self.capacity <= other.capacity

    def __ge__(self, other):
        """Defines behavior for the greater-than-or-equal-to operator, >=."""
        return self.capacity >= other.capacity

    @property
    def t_name(self):
        """Transport name property"""
        return self._t_name

    @t_name.setter
    def t_name(self, name):
        self._t_name = name

    @t_name.deleter
    def t_name(self):
        del self._t_name

    @property
    def driver(self):
        """Driver property"""
        return self._driver

    @driver.setter
    def driver(self, person):
        self._driver = person

    @driver.deleter
    def driver(self):
        del self._driver
        self._driver = None

    @classmethod
    def with_random_driver(cls, t_name, capacity):
        """Create transport class with random driver"""
        driver = cls._get_random_driver()
        return cls(t_name, driver, capacity)

    @classmethod
    def _get_random_driver(cls):
        """Create a random driver"""
        names = ['Liam', 'Noah', 'Oliver']
        d_name = random.choice(names)
        d_money = random.randrange(0, 1000, 10)
        driver_rand = Passanger(d_name, d_money)
        return driver_rand

    @staticmethod
    def destroy(transport):
        """Destroy transport"""
        transport.capacity = 0
        del transport.driver
        transport.passangers.clear()
        return transport

    @abstractmethod
    def move(self):
        """Get the transport going"""

    @abstractmethod
    def stop(self):
        """Stop the transport"""

    def add_passanger(self, passanger):
        """Add passanger to the transport"""
        if len(self.passangers) < self.capacity:
            self.passangers.append(passanger)
        else:
            print('The transport is full')

    def remove_passanger(self, passanger):
        """Let the passanger off the transport"""
        try:
            self.passangers.remove(passanger)
        except ValueError:
            print(f"No such passanger inside {self.t_name}")


class PublicTransport(Transport):
    """Abstract class for public transport"""

    def __init__(self, t_name, driver, capacity, faire_price):
        """Same as Transport __init__ but with faire price """
        super().__init__(t_name, driver, capacity)
        self._faire_price = faire_price

    @property
    def faire_price(self):
        """Faire price attribute"""
        return self._faire_price

    @faire_price.setter
    def faire_price(self, price):
        self._faire_price = price

    @faire_price.deleter
    def faire_price(self):
        del self._faire_price

    @classmethod
    def with_random_driver(cls, t_name, capacity, faire_price):
        """Return """
        driver = cls._get_random_driver()
        return cls(t_name, driver, capacity, faire_price)

    @abstractmethod
    def message_to_passengers(self, message):
        """Send a message to all passangers"""

    def add_passanger(self, passanger):
        """Collect faire before taking a passanger abort"""
        passanger.pay(self.faire_price)
        super().add_passanger(passanger)


class Bus(PublicTransport):
    """A simple buss for carrying people"""

    def __repr__(self):
        return f"Bus[driver: {self.driver},\
transport: {self.t_name}, \
capacity: {self.capacity}, \
passangers: {self.passangers}]"

    def move(self):
        print(f"Hooray, the bus '{self.t_name}' is moving!")

    def stop(self):
        print(f"Here, the bus '{self.t_name}' has stopped")

    def use_horn(self):
        """Use horn of your Bus"""
        print(f"Boooooo, it's {self.t_name}")

    def message_to_passengers(self, message):
        """Send message to all passangers"""
        print(f"Dear passengers of the bus '{self.t_name}', {message}")


class UndergroundTrain(PublicTransport):
    """A simple underground train for carrying people"""
    def move(self):
        print(f"Moving '{self.t_name}' into tunnel!")

    def stop(self):
        print(f"The '{self.t_name}' has arrived at the station")

    def use_horn(self):
        """Use horn of your Train"""
        print(f"Booo Booo, it's {self.t_name}")

    def message_to_passengers(self, message):
        print(f"Dear passengers of the train '{self.t_name}', {message}")


class Scooter(Transport):
    """A simple scooter to have some fun"""
    def move(self):
        print("Scooters! I love scooters")

    def stop(self):
        print("Scooter stopped. I want to feel the wind again...")

    def fast_parcking(self):
        """Parc scooter somewhere"""
        print(f"I'm {self.t_name} and I am parked")


class Car(Transport):
    """A simple car for driving around"""

    def move(self):
        print(f"My brand new car {self.t_name}, take me far away")

    def stop(self):
        print("The car is stopped")

    def air_conditioning(self):
        """Add some cool air into the car"""
        print(f"Cool air, thank you, {self.t_name}")


class Transformer(Car, Scooter):
    """A simple transformer from Cybertron"""

    def fight(self):
        """Engage in furious fight"""
        print(f"Piy piy, I am {self.t_name}")


class Passanger:
    """A simple passanger"""
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __repr__(self):
        """String representation of Passanger"""
        return f"Passanger[name: {self.name}, money: {self.money}]"

    def __hash__(self):
        return hash(self.name + str(self.money))

    def __eq__(self, other):
        return (self.money == other.money) and (self.name == other.name)

    def pay(self, price):
        """Pay some money for services"""
        if self.money >= price:
            self.money -= price
            print(f"Paid {price} : {self}")
        else:
            print("No money no honey")


if __name__ == '__main__':
    # Tests
    print("*" * 50)
    print("Creating passangers...")
    alex = Passanger('Alex', 50)
    emma = Passanger('Emma', 40)
    john = Passanger('John', 100)
    nick = Passanger('Nick', 20)
    tom = Passanger('Tom', 30)
    print("Passangers created")
    print([alex, emma, john, nick, tom])

    print("*" * 50)
    print("Testing passanger")
    nick.pay(10)
    nick.pay(10)
    nick.pay(10)
    print("*" * 50)

    print("Testing bus...")
    ikarus = Bus('Ikarus', Passanger('Sam', 1000), capacity=30, faire_price=10)
    print("Adding passangers...")
    ikarus.add_passanger(alex)
    print(ikarus)
    ikarus.add_passanger(emma)
    print(ikarus)

    print("Testing methods of bus...")
    ikarus.message_to_passengers("we are starting our journey")
    ikarus.move()
    ikarus.use_horn()
    ikarus.stop()
    ikarus.message_to_passengers("thank you")
    print("*" * 50)

    print("Testing car...")
    nissan = Car('Nissan', Passanger('Tobby', 600), 4)
    # Overstuffing nissan
    for _ in range(5):
        print("Adding passanger")
        nissan.add_passanger(alex)
        print(nissan)

    # Empty nissan
    for _ in range(5):
        print("Removing passanger")
        nissan.remove_passanger(alex)
        print(nissan)

    print("*" * 50)
    print("Testing Trasnformer...")
    optimus_prime = Transformer("Optimus Prime", Passanger("Optimus", 9999), 0)
    optimus_prime.fight()
    optimus_prime.fast_parcking()
    optimus_prime.air_conditioning()
    optimus_prime.move()
    print("*" * 50)

    # ======================
    # Magic methods testing
    # ======================

    print("Testing magic methods...")
    driver_tim = Passanger("Tim", 850)
    sprinter = Bus("Sprinter", driver_tim, capacity=15, faire_price=5)
    sprinterCopy = Bus("Sprinter", driver_tim, capacity=15, faire_price=5)
    mazda = Car("Mazda", driver_tim, capacity=4)

    # __hash__
    print("hash(sprinter) = " + str(hash(sprinter)))
    print("hash(sprinterCopy) = " + str(hash(sprinterCopy)))
    print("hash(sprinter) = hash(sprinterCopy) :", hash(sprinter) == hash(sprinterCopy))

    # __eq__
    print("Sprinter == SprinterCopy: ", sprinter == sprinterCopy)

    # __lt__
    print("sprinter < mazda:", sprinter < mazda)

    # __gt__
    print("sprinter > mazda:", sprinter > mazda)

    # __le__
    print("sprinter <= mazda:", sprinter <= mazda)
    print("sprinter <= sprinterCopy:", sprinter <= sprinterCopy)

    # __ge__
    print("sprinter >= mazda:", sprinter >= mazda)
    print("sprinter >= sprinterCopy:", sprinter >= sprinterCopy)

    # ======================
    # Decorators testing
    # ======================

    # Class method
    paz = Bus.with_random_driver('PAZ', capacity=25, faire_price=10)
    print("Random bus driver:", paz.driver)

    audi = Car.with_random_driver("Audi", capacity=2)
    print("Random car driver:", audi.driver)

    # Static function
    print("Before destroying :", ikarus)
    paz = Transport.destroy(ikarus)
    print("After destroying :", ikarus)
