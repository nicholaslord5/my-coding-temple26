from database import connect_to_database

class User:
    def __init__(self, user_name, library_ID):
        self.__user_name = user_name
        self.__library_ID = library_ID

    def add_to_database(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)", (self.__user_name, self.__library_ID))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"User '{self.__user_name}' added to the database successfully.")

    @staticmethod
    def get_user_details(library_id):
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT name, library_id FROM users WHERE library_id = %s", (library_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return {"name": result[0], "library_id": result[1]}
        else:
            print("User not found.")
            return None

    @staticmethod
    def get_all_users():
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT name, library_id FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return [{"name": user[0], "library_id": user[1]} for user in users]

