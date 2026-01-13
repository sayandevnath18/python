from bus import Bus
from passenger import Passenger
from company import BusCompany


def main():
    company = BusCompany()

    while True:
        print("\n===== BUS MANAGEMENT SYSTEM =====")
        print("1. Add Bus")
        print("2. Show All Buses")
        print("3. Book Seat")
        print("4. Show Seat Status")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            coach = int(input("Coach No: "))
            driver = input("Driver Name: ")
            arrival = input("Arrival Time: ")
            departure = input("Departure Time: ")
            source = input("From: ")
            destination = input("To: ")

            bus = Bus(coach, driver, arrival, departure, source, destination)
            company.add_bus(bus)

        elif choice == "2":
            company.show_buses()

        elif choice == "3":
            coach = int(input("Coach No: "))
            seat = int(input("Seat No (1-20): "))
            name = input("Passenger Name: ")
            phone = input("Phone: ")

            passenger = Passenger(name, phone)
            company.book_seat(coach, seat, passenger)

        elif choice == "4":
            coach = int(input("Coach No: "))
            company.show_seats(coach)

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
