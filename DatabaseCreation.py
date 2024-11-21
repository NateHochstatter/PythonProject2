import sqlite3
#testing
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS Score;")
cursor.execute("DROP TABLE IF EXISTS Student;")
cursor.execute("DROP TABLE IF EXISTS User;")

# Create User table
cursor.execute("CREATE TABLE IF NOT EXISTS User (" +
               "username VARCHAR(32) NOT NULL,password VARCHAR(32) NOT NULL, primary key (username));")

# Create Student table
cursor.execute("CREATE TABLE IF NOT EXISTS Student (" +
               "id VARCHAR(9) NOT NULL, name VARCHAR(32) NOT NULL, age INTEGER NOT NULL, " +
               "gender VARCHAR(1), major VARCHAR(32), phone VARCHAR(32), UNIQUE (id), primary key (id));")

# Create Score table
cursor.execute("CREATE TABLE IF NOT EXISTS Score (" +
               "id VARCHAR(9) NOT NULL, name VARCHAR(32) NOT NULL, CS_1030 INTEGER," +
               " CS_1100 INTEGER, CS_2030 INTEGER, UNIQUE (id), primary key (id));")

# Insert data into User table
cursor.execute("INSERT INTO User (username, password) VALUES " +
               "('1', '1'), ('Emily', '!Password1'), ('Bob', '@YesWeCan4'), ('Jason', '@Whatmat4');")
#note the 1, 1 are made for quick and easy logins

# Insert data into Student table
cursor.execute(" INSERT INTO Student (id, name, age, gender, major, phone) VALUES " +
               "('700300001', 'Emily White', 20, 'F', 'CS', '816-111-1111'), " +
               "('700300002', 'Bob Builder', 21, 'M', 'CYBR', '816-222-2222'), " +
               "('700300003', 'Jason James', 22, 'M', 'SE', '816-333-3333');")

# Insert data into Score table
cursor.execute("INSERT INTO Score (id, name, CS_1030, CS_1100, CS_2030) VALUES " +
               "('700300001', 'Emily White', 85, 90, 88), ('700300002', 'Bob Builder', 78, 82, 80), " +
               "('700300003', 'Jason James', 92, 95, 94);")

# Commit changes and close the connection
conn.commit()

# Select and display all records from User table
print("User Table:")
cursor.execute("SELECT * FROM User;")
users = cursor.fetchall()
for user in users:
    print(user)

# Select and display all records from Student table
print("\nStudent Table:")
cursor.execute("SELECT * FROM Student;")
students = cursor.fetchall()
for student in students:
    print(student)

# Select and display all records from Score table
print("\nScore Table:")
cursor.execute("SELECT * FROM Score;")
scores = cursor.fetchall()
for score in scores:
    print(score)

conn.close()

print("Tables created and data inserted successfully.")