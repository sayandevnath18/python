class Menu:
    """
    Menu class represents the restaurant's food menu.
    Allows adding, finding, removing, and displaying food items.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Add a FoodItem object to the menu.
        """
        self.items.append(item)
        print(f"\n✅ '{item.name}' added to the menu.")

    def find_item(self, item_name):
        """
        Search for a FoodItem by name (case-insensitive).
        Returns the item if found, else None.
        """
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        """
        Remove a FoodItem from the menu by name.
        """
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"\n🗑️ Item '{item_name}' deleted from the menu.")
        else:
            print(f"\n❌ Item '{item_name}' not found in the menu.")

    def show_item(self):
        """
        Display all food items in the menu with price and quantity.
        """
        if not self.items:
            print("\n⚠️ Menu is empty!")
            return

        print("\n🍽️ MENU")
        print(f"{'Name':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for item in self.items:
            print(f"{item.name:<20} {item.price:<10} {item.quantity:<10}")
