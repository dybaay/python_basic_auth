from dbConnect import *
from helpers.helper import *


def close_db_connection():
    cursor.close()
    conn.close()


class Login:
    def __init__(self):
        self.username = ""
        self.password = ""

    def get_credentials(self):
        self.username = input("Input username: ")
        self.password = input("Input password: ")

    def authenticate(self):
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (self.username,))
        user = cursor.fetchone()

        if user:
            if password_check(self.password, user['password']):
                print("logged in successful")
            else:
                print("Invalid credentials provided")
        else:
            print("user does not exist")

    def main(self):
        try:
            self.get_credentials()
            self.authenticate()
        except mysql.connector.Error as err:
            print(f"Error {err}")
        finally:
            close_db_connection()


if __name__ == "__main__":
    login = Login()
    login.main()
