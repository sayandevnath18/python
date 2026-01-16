from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, location):
        self.name = name
        self.location = location

    @abstractmethod
    def profile(self):
        pass


class Rider(User):
    def __init__(self, name, location, balance):
        super().__init__(name, location)
        self.balance = balance
        self.current_ride = None

    def profile(self):
        print(f"Rider: {self.name}, Balance: {self.balance}")


class Driver(User):
    def __init__(self, name, location, vehicle):
        super().__init__(name, location)
        self.vehicle = vehicle
        self.available = True
        self.earnings = 0

    def profile(self):
        print(f"Driver: {self.name}, Vehicle: {self.vehicle.vehicle_type}")
