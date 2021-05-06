"""This module is used to implement OOP concepts in Python"""

from abc import ABC, abstractmethod


class Transport(ABC):
    """Abstract class for transport"""

    def __init__(self, t_name, driver, capacity):
        """Transport should have name, driver and optionally some passangers"""
        self.driver = driver
        self.passangers = []
        self.t_name = t_name
        self.capacity = capacity


    def __repr__(self):
        return f"Transport[driver: {self.driver},\
transport: {self.t_name}, \
capacity: {self.capacity}, \
passangers: {self.passangers}]"

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
        self.faire_price = faire_price

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
