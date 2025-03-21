import json
import os

BOOKS_FILE = "OPP/books.json"

# Ensure the directory and file exist
def initialize_file():
    os.makedirs(os.path.dirname(BOOKS_FILE), exist_ok=True)
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as file:
            json.dump([], file)  # Initialize with an empty list

# Load books from file
def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file is empty or invalid

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Add a book
def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter book author: ")
    books.append({"title": title, "author": author, "available": True})
    print(f"Book '{title}' added successfully!")
    save_books(books)  # Save books after adding

# Display all books
def display_books(books):
    if not books:
        print("No books in the library.")
    else:
        print("\n--- Books in the Library ---")
        for book in books:
            status = "Available" if book["available"] else "Borrowed"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")

# Borrow a book
def borrow_book(books):
    title = input("Enter the book title to borrow: ")
    for book in books:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print(f"Book '{title}' borrowed successfully!")
            else:
                print(f"Book '{title}' is already borrowed.")
            save_books(books)  # Save books after borrowing
            return
    print(f"Book '{title}' not found in the library.")

# Return a book
def return_book(books):
    title = input("Enter the book title to return: ")
    for book in books:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print(f"Book '{title}' returned successfully!")
            else:
                print(f"Book '{title}' is already available.")
            save_books(books)  # Save books after returning
            return
    print(f"Book '{title}' not found in the library.")

# Main function
def main():
    initialize_file()  # Ensure the file exists and is initialized
    books = load_books()  # Load books when the program starts

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()