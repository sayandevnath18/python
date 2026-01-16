from ride import Ride
from matching import RideMatcher


class RideService:
    def __init__(self):
        self.drivers = []
        self.riders = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_rider(self, rider):
        self.riders.append(rider)

    def request_ride(self, rider, vehicle_type, distance):
        driver = RideMatcher.find_driver(self.drivers, vehicle_type)

        if not driver:
            print("No driver available")
            return None

        driver.available = False
        ride = Ride(rider, driver, distance)
        ride.start()
        rider.current_ride = ride
        return ride
