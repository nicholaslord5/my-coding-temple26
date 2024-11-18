from library.book import Book
from library.user import User
from library.author import Author

def main_menu():
    while True:
        print("\nWelcome to the Library Management System\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def user_menu():
    print("\nUser Operations:")
    while True:
        print("1. Add a new user\n2. View user details\n3. Display all users\n4. Go Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(user_name, library_id)
            user.add_to_database()
        elif choice == '2':
            library_id = input("Enter library ID to view details: ")
            user_data = User.get_user_details(library_id)
            if user_data:
                print(f"User: {user_data['name']}, Library ID: {user_data['library_id']}")
            else:
                print("User not found.")
        elif choice == '3':
            users = User.get_all_users()
            print("\nList of all users:")
            for user in users:
                print(f"User: {user['name']}, Library ID: {user['library_id']}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def book_menu():
    print("\nBook Operations:")
    while True:
        print("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Go Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author ID: ")
            genre = input("Enter genre: ")
            pub_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(title, author, genre, pub_date)
            book.add_to_database()
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            book_data = Book.search_book(title)
            if book_data and book_data["availability"]:
                book = Book(title, book_data["genre"], book_data["publication_date"])
                if book.borrow():
                    print(f"You have successfully borrowed '{title}'.")
            else:
                print("Book is not available or does not exist.")
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            book_data = Book.search_book(title)
            if book_data:
                book = Book(title, book_data["genre"], book_data["publication_date"])
                book.return_book()
                print(f"You have returned '{title}'.")
            else:
                print("Book not found.")
        elif choice == '4':
            title = input("Enter the title to search for: ")
            book_data = Book.search_book(title)
            if book_data:
                print(f"Book found: {book_data}")
            else:
                print("Book not found.")
        elif choice == '5':
            books = Book.display_all_books()
            print("\nList of all books:")
            for book in books:
                print(f"Title: {book['title']}, Genre: {book['genre']}, "
                      f"Publication Date: {book['publication_date']}, Available: {book['availability']}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def author_menu():
    print("\nAuthor Operations:")
    while True:
        print("1. Add a new author\n2. View author details\n3. Display all authors\n4. Go Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            author.add_to_database()
        elif choice == '2':
            name = input("Enter the author's name to view details: ")
            author_data = Author.get_author_details(name)
            if author_data:
                print(f"Author: {author_data['name']}, Biography: {author_data['biography']}")
            else:
                print("Author not found.")
        elif choice == '3':
            authors = Author.get_all_authors()
            print("\nList of all authors:")
            for author_name in authors:
                print(f"Author: {author_name}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")
