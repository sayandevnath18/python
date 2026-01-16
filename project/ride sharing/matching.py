class RideMatcher:
    @staticmethod
    def find_driver(drivers, vehicle_type):
        for driver in drivers:
            if driver.available and driver.vehicle.vehicle_type == vehicle_type:
                return driver
        return None
