from enum import Enum
from datetime import datetime


class RideStatus(Enum):
    REQUESTED = 1
    ONGOING = 2
    COMPLETED = 3


class Ride:
    def __init__(self, rider, driver, distance):
        self.rider = rider
        self.driver = driver
        self.distance = distance
        self.status = RideStatus.REQUESTED
        self.fare = self.calculate_fare()
        self.start_time = None
        self.end_time = None

    def calculate_fare(self):
        return self.distance * self.driver.vehicle.rate_per_km

    def start(self):
        self.status = RideStatus.ONGOING
        self.start_time = datetime.now()

    def complete(self):
        if self.rider.balance < self.fare:
            raise Exception("Insufficient balance")

        self.status = RideStatus.COMPLETED
        self.end_time = datetime.now()
        self.rider.balance -= self.fare
        self.driver.earnings += self.fare
        self.driver.available = True
