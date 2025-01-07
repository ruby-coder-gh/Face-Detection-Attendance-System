import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Data to insert into the table (use actual values instead of placeholders)
department = "Computer Science"
course = "Data Structures"
year = "2"
semester = "Spring"
student_name = "John Doe"
student_id = "12345"
gender = "Male"
age = 20
address = "123 Main St"
phone_number = "123-456-7890"
email = "johndoe@example.com"
grade = "A"
attendance_status = "Present"

# SQL query to insert data into the student table
cursor.execute('''
INSERT INTO student (department, course, year, semester, student_name, student_id, gender, age, address, phone_number, email, grade, attendance_status)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
''', (department, course, year, semester, student_name, student_id, gender, age, address, phone_number, email, grade, attendance_status))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")
