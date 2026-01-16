from users import Rider, Driver
from vehicle import Car, Bike
from service import RideService


service = RideService()

r1 = Rider("Rahim", "Tekota", 500)
d1 = Driver("Kamal", "Chittagong", Car())
d2 = Driver("Jamal", "Anowara", Bike())

service.add_rider(r1)
service.add_driver(d1)
service.add_driver(d2)

ride = service.request_ride(r1, "car", 10)

if ride:
    print("Ride started")
    ride.complete()
    print("Ride completed")
    r1.profile()
    d1.profile()
