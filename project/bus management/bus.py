from abc import ABC, abstractmethod


class AbstractBus(ABC):
    def __init__(self, coach_no, driver, arrival, departure, source, destination):
        self.coach_no = coach_no
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.source = source
        self.destination = destination
        self.seats = [None] * 20

    @abstractmethod
    def bus_info(self):
        pass


class Bus(AbstractBus):
    def bus_info(self):
        return (
            f"{self.coach_no}\t{self.driver}\t{self.arrival}\t"
            f"{self.departure}\t{self.source}\t{self.destination}"
        )
