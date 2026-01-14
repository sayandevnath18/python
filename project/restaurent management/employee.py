from user import User


class Employee(User):
    """
    Employee class represents a restaurant staff member.
    Stores personal and job-related information.
    """

    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
