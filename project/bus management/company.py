from bus import Bus
from passenger import Passenger


class BusCompany:
    def __init__(self):
        self.buses = {}

    def add_bus(self, bus):
        self.buses[bus.coach_no] = bus
        print("Bus added successfully!")

    def show_buses(self):
        if not self.buses:
            print("No buses available!")
            return

        print("Coach\tDriver\tArrival\tDeparture\tFrom\tTo")
        for bus in self.buses.values():
            print(bus.bus_info())

    def book_seat(self, coach_no, seat_no, passenger):
        if coach_no not in self.buses:
            print("Invalid coach number!")
            return

        bus = self.buses[coach_no]

        if not 1 <= seat_no <= 20:
            print("Invalid seat number!")
            return

        if bus.seats[seat_no - 1] is None:
            bus.seats[seat_no - 1] = passenger
            print("Seat booked successfully!")
        else:
            print("Seat already booked!")

    def show_seats(self, coach_no):
        if coach_no not in self.buses:
            print("Invalid coach number!")
            return

        bus = self.buses[coach_no]
        for i, seat in enumerate(bus.seats, start=1):
            status = "Empty" if seat is None else str(seat)
            print(f"Seat {i}: {status}")
