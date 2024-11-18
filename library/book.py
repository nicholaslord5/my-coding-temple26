from database import connect_to_database

class Book:
    def __init__(self, title, author, genre, publication_date, availability=True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = availability

    def add_to_database(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author_id, genre, publication_date, availability) VALUES (%s, %s, %s, %s, %s)",
            (self.__title, self.__author, self.__genre, self.__publication_date, self.__availability)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Book '{self.__title}' added successfully to the database.")

    def borrow(self):
        if self.__availability:
            conn = connect_to_database()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET availability = 0 WHERE title = %s", (self.__title,))
            conn.commit()
            cursor.close()
            conn.close()
            self.__availability = False
            return True
        return False

    def return_book(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET availability = 1 WHERE title = %s", (self.__title,))
        conn.commit()
        cursor.close()
        conn.close()
        self.__availability = True

    @staticmethod
    def search_book(title):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT title, genre, publication_date, availability FROM books WHERE title = %s", (title,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return {
                "title": result[0],
                "genre": result[1],
                "publication_date": result[2],
                "availability": bool(result[3])
            }
        else:
            print("Book not found.")
            return None

    @staticmethod
    def display_all_books():
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT title, genre, publication_date, availability FROM books")
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return [
            {"title": book[0], "genre": book[1], "publication_date": book[2], "availability": bool(book[3])}
            for book in books
        ]