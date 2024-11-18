from database import connect_to_database

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def add_to_database(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name, biography) VALUES (%s, %s)",
            (self.__name, self.__biography)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Author '{self.__name}' added to the database successfully.")

    @staticmethod
    def get_author_details(name):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT name, biography FROM authors WHERE name = %s", (name,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return {"name": result[0], "biography": result[1]}
        else:
            print("Author not found.")
            return None

    @staticmethod
    def get_all_authors():
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM authors")
        authors = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return authors