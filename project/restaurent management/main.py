from admin import Admin
from customer import Customer
from employee import Employee
from food_item import FoodItem
from restaurent import Restaurent

# ================== RESTAURANT SETUP ==================
restaurent = Restaurent("🍽️ Python Restaurant")


# ================== CUSTOMER MENU ==================
def customer_menu():
    print("\n" + "=" * 50)
    print("👤 CUSTOMER REGISTRATION")
    print("=" * 50)

    name = input("👉 Enter your name: ")
    phone = input("👉 Enter your phone number: ")
    email = input("👉 Enter your email: ")
    address = input("👉 Enter your address: ")

    customer = Customer(name, phone, email, address)

    while True:
        print("\n" + "-" * 50)
        print(f"🙏 Welcome to {restaurent.name}, {customer.name}!")
        print("-" * 50)
        print("1️⃣  View Menu")
        print("2️⃣  Add Item to Cart")
        print("3️⃣  View Cart")
        print("4️⃣  Pay Bill")
        print("5️⃣  Exit")
        print("-" * 50)

        choice = int(input("👉 Enter your choice (1-5): "))

        if choice == 1:
            customer.view_menu(restaurent)

        elif choice == 2:
            item_name = input("🍔 Enter item name: ")
            item_quantity = int(input("🔢 Enter quantity: "))
            customer.add_to_cart(restaurent, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            total = customer.cart.total_price()
            print(f"\n💳 Total Bill: {total} Tk")
            print("✅ Payment Successful!")
            customer.cart.clear()

        elif choice == 5:
            print("👋 Thank you for visiting!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# ================== ADMIN MENU ==================
def admin_menu():
    print("\n" + "=" * 50)
    print("🛠️  ADMIN LOGIN")
    print("=" * 50)

    name = input("👉 Enter your name: ")
    phone = input("👉 Enter your phone number: ")
    email = input("👉 Enter your email: ")
    address = input("👉 Enter your address: ")

    admin = Admin(name, phone, email, address)

    while True:
        print("\n" + "-" * 50)
        print(f"🔐  Welcome Admin {admin.name}!")
        print("-" * 50)
        print("1️⃣  Add Employee")
        print("2️⃣  Add Food Item")
        print("3️⃣  View Employees")
        print("4️⃣  View Food Items")
        print("5️⃣  Remove Food Item")
        print("6️⃣  Exit")
        print("-" * 50)

        choice = int(input("👉 Enter your choice (1-6): "))

        if choice == 1:
            print("\n👨‍🍳 ADD EMPLOYEE")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            age = input("Age: ")
            designation = input("Designation: ")
            salary = int(input("Salary: "))

            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(restaurent, employee)

        elif choice == 2:
            print("\n🍕 ADD FOOD ITEM")
            name = input("Item Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            item = FoodItem(name, price, quantity)
            admin.add_item(restaurent, item)

        elif choice == 3:
            admin.view_employee(restaurent)

        elif choice == 4:
            admin.view_item(restaurent)

        elif choice == 5:
            item_name = input("❌ Enter item name to remove: ")
            admin.remove_item(restaurent, item_name)

        elif choice == 6:
            print("🚪 Logging out admin...")
            break

        else:
            print("❌ Invalid choice! Try again.")


# ================== MAIN PROGRAM ==================
while True:
    print("\n" + "=" * 50)
    print("🍽️  WELCOME TO PYTHON RESTAURANT")
    print("=" * 50)
    print("1️⃣  Customer")
    print("2️⃣  Admin")
    print("3️⃣  Exit")
    print("-" * 50)

    choice = int(input("👉 Enter your choice (1-3): "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print("\n🙏 Thank you! See you again.")
        break
    else:
        print("❌ Invalid choice! Please select again.")
