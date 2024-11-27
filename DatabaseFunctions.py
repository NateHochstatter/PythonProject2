import sqlite3

def addStudent(ID, name, age, gender, major, phone):

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Inserts new student information into the database
        cursor.execute("INSERT INTO Student (id, name, age, gender, major, phone) VALUES (?, ?, ?, ?, ?, ?)",
                       (ID, name, age, gender, major, phone))

def showAllStudents():
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Selects all students
        cursor.execute("SELECT * FROM Student")

        students = cursor.fetchall()

        #Header
        #printPage("StudentRecord.txt")
        print(f"{'ID':<8} {'Name':<15} {'Phone':<15} {'Major':<5}")
        for student in students:
            print(student) #Note: needs formatting so it doesn't just show the raw data
        print()

def showStudentName(name):
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Displays a student based on their name
        cursor.execute("SELECT * FROM Student WHERE name = ?", (name,))

        printPage("StudentRecord.txt")
        students = cursor.fetchall()

        if students:
            for student in students:
                print(i) #Note: needs formatting so it doesn't just show the raw data
            print()

def showStudentID(ID):
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Displays a student based on their ID
        cursor.execute("SELECT * FROM Student WHERE id = ?", (ID,))

        printPage("StudentRecord.txt")
        student = cursor.fetchone()
        print(student) #Note: needs formatting so it doesn't just show the raw data
        
def deleteStudent(ID):

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor= conn.cursor()

        #Deletes student information from the database
        cursor.execute("DELETE FROM Student WHERE id = ?", (ID,))

def showScoreName(name):

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Selects students based on their name
        cursor.execute("SELECT * FROM Score WHERE name = ?", (name,))

        #Header
        #printPage("StudentRecord.txt")
        print(f"{'ID':<8} {'Name':<15} {'Phone':<15} {'Major':<5}") #Note: 'Phone' and 'Major' need to be replaced with classes

        #Displays student scores
        students = cursor.fetchall()
        for student in students:
            print(student) #Note: needs formatting so it doesn't just show the raw data
        print()
    
def showScoreID(ID):

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Selects student based on their ID
        cursor.execute("SELECT * FROM Score WHERE id = ?", (ID,))

        #Header
        #printPage("StudentRecord.txt")
        print(f"{'ID':<8} {'Name':<15} {'Phone':<15} {'Major':<5}") #Note: 'Phone' and 'Major' need to be replaced with classes

        #Displays student scores
        students = cursor.fetchall()
        for student in students:
            print(student) #Note: needs formatting so it doesn't just show the raw data
        print()
