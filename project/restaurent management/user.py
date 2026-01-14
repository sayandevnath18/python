class User:
    """
    Base User class representing a person in the system.
    Stores common attributes like name, phone, email, and address.
    """

    def __init__(self, name: str, phone: str, email: str, address: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        """
        Return a readable string representation of the User.
        """
        return f"{self.name} | Phone: {self.phone} | Email: {self.email} | Address: {self.address}"
