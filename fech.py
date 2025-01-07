import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('student.db')  # Make sure the path is correct
cursor = conn.cursor()

# Query to fetch all records from the student table
cursor.execute("SELECT * FROM student")

# Fetch all rows
rows = cursor.fetchall()

# Display the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
