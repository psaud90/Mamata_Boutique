import sqlite3

connection = sqlite3.connect("boutique.db")

cursor = connection.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    password TEXT NOT NULL

)
""")

# Check if admin already exists
cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))

user = cursor.fetchone()

if user is None:

    cursor.execute("""

    INSERT INTO users(username,password)

    VALUES(?,?)

    """, ("admin", "1234"))

    print("Admin User Created Successfully!")

else:

    print("Admin Already Exists!")

connection.commit()

connection.close()