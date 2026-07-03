import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

password = hashlib.sha256("admin123".encode()).hexdigest()

cursor.execute("DELETE FROM users")

cursor.execute(
    "INSERT INTO users(username,password) VALUES(?,?)",
    ("admin", password)
)

conn.commit()
conn.close()

print("Database Created Successfully")
print("Username : admin")
print("Password : admin123")