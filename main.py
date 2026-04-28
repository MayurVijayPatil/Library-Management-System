import json
from pathlib import Path


DATA_FILE = Path("books.json")


class Book:
    def __init__(self, book_id, title, author, total_copies, available_copies=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies if available_copies is None else available_copies

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            int(data["total_copies"]),
            int(data["available_copies"]),
        )


class Library:
    def __init__(self, file_path=DATA_FILE):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def load_books(self):
        if not self.file_path.exists():
            self.books = self.sample_books()
            self.save_books()
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            self.books = [Book.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError, ValueError):
            print("Data file is invalid. Starting with an empty library.")
            self.books = []

    def save_books(self):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def sample_books(self):
        return [
            Book("B001", "Python Basics", "John Smith", 3),
            Book("B002", "Data Structures", "Anita Sharma", 2),
            Book("B003", "Clean Code", "Robert Martin", 1),
        ]

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id.lower() == book_id.lower():
                return book
        return None

    def add_book(self):
        print("\nAdd New Book")
        book_id = get_required_input("Enter book ID: ").upper()

        if self.find_book_by_id(book_id):
            print("Book ID already exists. Please use a different ID.")
            return

        title = get_required_input("Enter book title: ")
        author = get_required_input("Enter author name: ")
        total_copies = get_positive_number("Enter total copies: ")

        self.books.append(Book(book_id, title, author, total_copies))
        self.save_books()
        print("Book added successfully.")

    def view_books(self):
        print("\nAll Books")
        if not self.books:
            print("No books available in the library.")
            return

        print_books_table(self.books)

    def search_books(self):
        print("\nSearch Book")
        keyword = get_required_input("Enter title or author to search: ").lower()

        results = [
            book
            for book in self.books
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]

        if results:
            print_books_table(results)
        else:
            print("No matching books found.")

    def issue_book(self):
        print("\nIssue Book")
        book_id = get_required_input("Enter book ID: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print("Book not found.")
            return

        if book.available_copies <= 0:
            print("This book is currently not available.")
            return

        book.available_copies -= 1
        self.save_books()
        print(f"Book issued successfully: {book.title}")

    def return_book(self):
        print("\nReturn Book")
        book_id = get_required_input("Enter book ID: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print("Book not found.")
            return

        if book.available_copies >= book.total_copies:
            print("All copies of this book are already in the library.")
            return

        book.available_copies += 1
        self.save_books()
        print(f"Book returned successfully: {book.title}")

    def delete_book(self):
        print("\nDelete Book")
        book_id = get_required_input("Enter book ID: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print("Book not found.")
            return

        self.books.remove(book)
        self.save_books()
        print(f"Book deleted successfully: {book.title}")


def get_required_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number > 0:
                return number
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def print_books_table(books):
    print("-" * 82)
    print(f"{'ID':<8}{'Title':<26}{'Author':<22}{'Total':<10}{'Available':<10}")
    print("-" * 82)
    for book in books:
        print(
            f"{book.book_id:<8}"
            f"{book.title[:24]:<26}"
            f"{book.author[:20]:<22}"
            f"{book.total_copies:<10}"
            f"{book.available_copies:<10}"
        )
    print("-" * 82)


def show_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_books()
        elif choice == "4":
            library.issue_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            library.delete_book()
        elif choice == "7":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
