from book import Book
from user import User


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    # ---------- BOOK FUNCTIONS ----------
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))
        self.books.append(Book(book_id, title, author, quantity))
        print("✅ Book added successfully!\n")

    def display_books(self):
        if not self.books:
            print("📭 No books available.\n")
            return
        print("\n📚 Available Books:")
        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Qty: {book.quantity}")
        print()

    # ---------- USER FUNCTIONS ----------
    def add_user(self):
        user_id = input("Enter User ID: ")
        name = input("Enter User Name: ")
        self.users.append(User(user_id, name))
        print("👤 User added successfully!\n")

    def display_users(self):
        if not self.users:
            print("📭 No users found.\n")
            return
        print("\n👥 Registered Users:")
        for user in self.users:
            print(f"ID: {user.user_id}, Name: {user.name}")
        print()

    # ---------- ISSUE BOOK ----------
    def issue_book(self):
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID: ")

        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not user:
            print("❌ User not found.\n")
            return
        if not book:
            print("❌ Book not found.\n")
            return
        if book.quantity == 0:
            print("⚠️ Book out of stock.\n")
            return

        book.quantity -= 1
        user.issued_books.append(book.title)
        print(f"📕 Book issued to {user.name} successfully!\n")
