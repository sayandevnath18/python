from user import User


class Admin(User):
    """
    Admin class represents a system administrator.
    Admin can manage employees and food items of the restaurant.
    """

    def add_employee(self, restaurent, employee):
        """
        Add a new employee to the restaurant
        """
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        """
        Display all employees of the restaurant
        """
        restaurent.view_employee()

    def add_item(self, restaurent, item):
        """
        Add a food item to the restaurant menu
        """
        restaurent.menu.add_item(item)

    def view_item(self, restaurent):
        """
        Show all food items from the menu
        """
        restaurent.menu.show_item()

    def remove_item(self, restaurent, item_name):
        """
        Remove a food item from the menu by name
        """
        restaurent.menu.remove_item(item_name)
