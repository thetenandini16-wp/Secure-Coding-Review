import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter Username : ")
password = input("Enter Password : ")

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

try:
    cursor.execute(query)

    if cursor.fetchone():
        print("Login Successful")
    else:
        print("Invalid Login")

except Exception as e:
    print("Error :", e)

conn.close()