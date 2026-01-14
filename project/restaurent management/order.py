class Order:
    """
    Order class represents a customer's cart.
    Stores food items added by the customer along with quantity and price.
    """

    def __init__(self):
        # Dictionary format: {item_name: {"price": price, "quantity": quantity}}
        self.items = {}

    def add_item(self, item, quantity):
        """
        Add a FoodItem to the cart with specified quantity.
        If the item already exists, increase its quantity.
        """
        if item.name in self.items:
            self.items[item.name]["quantity"] += quantity
        else:
            self.items[item.name] = {
                "price": item.price,
                "quantity": quantity,
            }
        print(f"\n✅ Added {quantity} x '{item.name}' to cart.")

    def total_price(self):
        """
        Calculate the total price of items in the cart.
        """
        return sum(data["price"] * data["quantity"] for data in self.items.values())

    def clear(self):
        """
        Clear all items from the cart.
        """
        self.items = {}
        print("\n🧹 Cart has been cleared.")
