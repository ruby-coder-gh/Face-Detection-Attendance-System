import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create table with the updated column name 'student_id'
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dep TEXT NOT NULL,
    course TEXT NOT NULL,
    year TEXT NOT NULL,
    semester TEXT NOT NULL,
    div TEXT NOT NULL,
    id TEXT NOT NULL,
    roll INTEGER NOT NULL,
    gender TEXT NOT NULL,
    dob TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    teacher TEXT NOT NULL,
    photo BLOB
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully with 'student_id'!")
