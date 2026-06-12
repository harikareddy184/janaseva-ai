import sqlite3

# Connect to database (it will create database.db automatically)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

# Save changes and close connection
conn.commit()
conn.close()

print("Database created successfully!")