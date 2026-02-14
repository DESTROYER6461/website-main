import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    bio TEXT,
    instagram TEXT,
    linkedin TEXT,
    github TEXT
)
""")

# Insert sample user only once
cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO users (fullname, email, phone, address, bio, instagram, linkedin, github)
    VALUES ('DESTROYER', 'destroyer@mail.com', '+91 99999 99999', 'Bengaluru',
            'Student • Developer', 'insta.com', 'linkedin.com', 'github.com')
    """)

conn.commit()
conn.close()

print("Database initialized successfully!")
