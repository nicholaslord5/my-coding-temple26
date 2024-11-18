Library Management System with Database Integration

Overview

The Library Management System (LMS) is a command-line application designed to streamline the management of library resources, including books, authors, and users. This project integrates Python and MySQL to provide database management capabilities and scalability of the system.

The system is built upon an Object-Oriented Programming (OOP) foundation and includes database-enabled functionalities such as adding, borrowing, returning, and viewing library resources.

Modular Design: Classes for books, users, and authors encapsulate functionality and ensure clean, reusable code.
Database Integration: Each class has methods to interact with the database (e.g., add_to_database(), search_book()).
Error Handling: Safeguards against invalid inputs and database connection errors.

Project Structure

library-management-system/

|–– library/

│   |–– book.py          # Book module

│   |–– user.py          # User module

│   |–– author.py        # Author module

|

|–– database.py          # connects modules and SQL database

|–– main.py              # Main menu script

|–– README.md            # Project documentation


Features
1. Book Operations
Add new books to the library.
Borrow and return books with availability tracking.
Search for specific books by title.
Display a list of all books with detailed information.

2. User Operations
Register new users in the library system.
View details of a specific user, including borrowed books.
Display all registered users.

3. Author Operations
Add new authors to the library.
View an author's details, including their biography.
Display a list of all authors.

4. Database Integration
Persistence: All data is stored in a MySQL database, ensuring that no information is lost when the program is closed.
Scalability: Designed to handle large collections of books, authors, and users efficiently.
Relational Design: Ensures data integrity using relationships between tables.


System Design
1. Object-Oriented Modules
The system is built on the following OOP modules:
Book: Represents book-related data and actions.
User: Handles user details and borrowing history.
Author: Manages author-related information.

2. Database Tables
The system uses a MySQL database with the following tables:
Books: Stores book details, including title, author, genre, and availability.
Authors: Maintains author names and biographies.
Users: Records user details and library IDs.
Borrowed_Books: Tracks borrowed and returned books.


Installation
Prerequisites
Python 3.x installed on your system.
MySQL installed and running.
Python libraries: mysql-connector-python.


Setup Steps
Clone this repository to your local machine

Install the required Python library:
pip install mysql-connector-python

Create a MySQL database:
CREATE DATABASE library_management;

Import the SQL schema to set up the database tables:
mysql -u <username> -p library_management < schema.sql


# Example configuration
host = "localhost"
user = "your_username"
password = "your_password"
database = "library_management"


Usage

Run the main menu to start the Library Management System:
python main.py


Main Menu
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
Each operation leads to a submenu for managing respective data.
