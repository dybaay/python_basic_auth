import mysql.connector


try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Akin_@2546",
        database="python_auth"
    )
    print("Database connection successful")
    cursor = conn.cursor(dictionary=True)
except mysql.connector.Error as err:
    print(f"Error connecting to the db: {err}")

