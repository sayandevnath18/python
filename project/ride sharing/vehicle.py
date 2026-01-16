class Vehicle:
    def __init__(self, vehicle_type, rate_per_km):
        self.vehicle_type = vehicle_type
        self.rate_per_km = rate_per_km


class Car(Vehicle):
    def __init__(self):
        super().__init__("car", 30)


class Bike(Vehicle):
    def __init__(self):
        super().__init__("bike", 20)
