import sqlite3
#testing
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS Score;")
cursor.execute("DROP TABLE IF EXISTS Student;")
cursor.execute("DROP TABLE IF EXISTS User;")
cursor.execute("DROP TABLE IF EXISTS Dnd;")

# Create User table
cursor.execute("CREATE TABLE IF NOT EXISTS User (" +
               "username VARCHAR(32) NOT NULL,password VARCHAR(32) NOT NULL, primary key (username));")

# Create Student table
cursor.execute("CREATE TABLE IF NOT EXISTS Student (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32) NOT NULL, age INTEGER NOT NULL, " +
               "gender VARCHAR(1), major VARCHAR(32), phone VARCHAR(32));")

# Create Score table
cursor.execute("CREATE TABLE IF NOT EXISTS Score (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32) NOT NULL, CS_1030 INTEGER," +
               " CS_1100 INTEGER, CS_2030 INTEGER);")

# Create Dnd table
cursor.execute("CREATE TABLE IF NOT EXISTS Dnd (" +
               "characterId INTEGER PRIMARY KEY AUTOINCREMENT, studentId INTEGER, name VARCHAR(32) NOT NULL" +
               ", class VARCHAR(32) NOT NULL, race VARCHAR(32) NOT NULL, level VARCHAR(3) NOT NULL" +
               ", campaign VARCHAR(100) NOT NULL);")

# Insert data into User table
cursor.execute("INSERT INTO User (username, password) VALUES " +
               "('1', '1'), ('Emily', '!Password1'), ('Bob', '@YesWeCan4'), ('Jason', '@Whatmat4');")
#note the 1, 1 are made for quick and easy logins

# Insert data into Student table
cursor.execute(" INSERT INTO Student (id, name, age, gender, major, phone) VALUES " +
               "(700300001, 'Emily White', 20, 'F', 'CS', '816-111-1111')")

# Insert data into Score table
cursor.execute("INSERT INTO Score (id, name, CS_1030, CS_1100, CS_2030) VALUES " +
               "(700300001, 'Emily White', 85, 90, 88)")

# Insert data into Dnd table
cursor.execute("INSERT INTO Dnd (characterId, studentId, name, class, race, level, campaign) VALUES " +
               "(1, 700300001, 'Pete', 'Druid', 'Elf', '8', 'The Great Escape')")

# Commit changes and close the connection
conn.commit()

cursor.execute(" INSERT INTO Student (name, age, gender, major, phone) VALUES " +
               "('Bob Builder', 21, 'M', 'CYBR', '816-222-2222'), " +
               "('Jason James', 22, 'M', 'SE', '816-333-3333');")

cursor.execute("INSERT INTO Score (name, CS_1030, CS_1100, CS_2030) VALUES " +
               "('Bob Builder', 78, 82, 80), ('Jason James', 92, 95, 94);")

# Insert data into Dnd table
cursor.execute("INSERT INTO Dnd (studentId, name, class, race, level, campaign) VALUES " +
               "(700300001, 'King Charles', 'Paladin', 'Human', '20', 'The Black Forest'), " +
               "(700300002, 'Queen Charles', 'Cleric', 'Human', '20', 'The Black Forest')")

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

# Select and display all records from Dnd table
print("\nDnd Table:")
cursor.execute("SELECT * FROM Dnd;")
dnd = cursor.fetchall()
for character in dnd:
    print(character)

conn.close()

print("Tables created and data inserted successfully.")