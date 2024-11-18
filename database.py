import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="library_db"
    )