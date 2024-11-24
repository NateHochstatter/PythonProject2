import sqlite3

def addStudent(ID, name, age, gender, major, phone):

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Inserts new student information into the database
        cursor.execute("INSERT INTO Student (id, name, age, gender, major, phone) VALUES (?, ?, ?, ?, ?, ?)",
                       (ID, name, age, gender, major, phone))

def showStudentName(name):
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Displays a student based on their name
        cursor.execute("SELECT * FROM Student WHERE name = ?", (name,))

        #printPage("StudentRecord.txt")
        rows = cursor.fetchall()

        if rows:
            for i in rows:
                print(i)
            print()
        
def deleteStudent(ID):

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor= conn.cursor()

        #Deletes student information from the database
        cursor.execute("DELETE FROM Student WHERE id = ?", (ID,))
