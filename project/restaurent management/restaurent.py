from menu import Menu


class Restaurent:
    """
    Restaurent class represents a restaurant.
    Stores restaurant name, employees, and menu.
    """

    def __init__(self, name: str):
        self.name = name
        self.employees = []  # List of Employee objects
        self.menu = Menu()  # Menu object

    def add_employee(self, employee):
        """
        Add an Employee object to the restaurant.
        """
        self.employees.append(employee)
        print(f"\n✅ Employee '{employee.name}' has been added to {self.name}.")

    def view_employee(self):
        """
        Display all employees of the restaurant.
        """
        if not self.employees:
            print("\n⚠️ No employees found.")
            return

        print(f"\n👥 Employee List of {self.name}:")
        print(f"{'Name':<15} {'Phone':<15} {'Email':<25} {'Address'}")
        print("-" * 70)
        for emp in self.employees:
            print(f"{emp.name:<15} {emp.phone:<15} {emp.email:<25} {emp.address}")
