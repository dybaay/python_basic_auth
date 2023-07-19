from helpers.helper import *
from User import User
from dbConnect import conn, cursor


def seed_data():
    return [
        {"username": "user1", "password": "password1"},
        {"username": "user2", "password": "password2"},
        {"username": "user3", "password": "password3"},
        {"username": "user4", "password": "password4"},
        {"username": "user5", "password": "password5"},
        {"username": "user6", "password": "password6"}
    ]


def seed_db():
    data = seed_data()
    for row in data:
        user = User()
        user.create({
            "username": row.get('username'),
            "password": password_encrypt(row.get('password'))
        })
    print("Data seeded")
    cursor.close()
    conn.close()


def main():
    seed_db()


if __name__ == "__main__":
    main()
