from dbConnect import conn
import bcrypt

cursor = conn.cursor()


def seed_data():
    return [
        ("user1", "password1"),
        ("user2", "password2"),
        ("user3", "password3")
    ]


def encrypt_password(password: str):
    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_pass.decode("utf-8")


def seed_db():
    data = seed_data()
    for username, password in data:
        password_encrypted = encrypt_password(password)
        query = "INSERT INTO users(username, password) VALUES (%s, %s)"
        values = (username, password_encrypted)
        cursor.execute(query, values)
    conn.commit()
    print("Data seeded")


def main():
    seed_db()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
