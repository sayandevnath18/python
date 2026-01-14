class FoodItem:
    """
    FoodItem class represents a single food item in the restaurant menu.
    Stores name, price, and available quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        Return a readable string representation of the FoodItem.
        """
        return f"{self.name} - Price: {self.price} Tk, Available: {self.quantity}"
