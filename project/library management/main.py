from library import Library


def main():
    library = Library()

    while True:
        print("====== Library Management System ======")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Add User")
        print("4. Display Users")
        print("5. Issue Book")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            library.add_user()
        elif choice == "4":
            library.display_users()
        elif choice == "5":
            library.issue_book()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice!\n")


if __name__ == "__main__":
    main()
