from user import User
from order import Order


class Customer(User):
    """
    Customer class represents a restaurant customer.
    Customers can view menu, add food items to cart and view cart.
    """

    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        """
        Display all available food items from the restaurant menu
        """
        restaurent.menu.show_item()

    def add_to_cart(self, restaurent, item_name, quantity):
        """
        Add selected food item to the customer's cart
        """
        item = restaurent.menu.find_item(item_name)

        if not item:
            print("\n❌ Item not found!")
            return

        if quantity > item.quantity:
            print("\n⚠️ Item quantity exceeded!")
            return

        item.quantity -= quantity
        self.cart.add_item(item, quantity)
        print("\n✅ Item added to cart successfully")

    def view_cart(self):
        """
        Display all items added to the cart with total price
        """
        print("\n" + "-" * 30)
        print("🛒 YOUR CART")
        print("-" * 30)
        print(f"{'Name':<10} {'Price':<10} {'Quantity'}")

        for name, data in self.cart.items.items():
            print(f"{name:<10} {data['price']:<10} {data['quantity']}")

        print("-" * 30)
        print(f"💰 Total Price: {self.cart.total_price()} Tk")
