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
        printPage("StudentRecord.txt")
        print(f"{'ID':<10} {'Name':<16} {'Phone':<15} {'Major':<5}")

        #Iterate through every student
        for student in students:

            #Unpack student into multiple variables
            stud_id, name, age, gender, major, phone = student

            #Display the relevant student information
            print(f"{stud_id:<10} {name:<16} {phone:<15} {major:<5}")
        print()

def showStudentName(name):
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Selects all students with a certain name
        cursor.execute("SELECT * FROM Student WHERE name = ?", (name,))

        students = cursor.fetchall()
        
        #Header
        printPage("StudentRecord.txt")
        print(f"{'ID':<10} {'Name':<16} {'Phone':<15} {'Major':<5}")

        if students:
            
            #Iterate through students
            for student in students:

                #Unpack student into multipel variables
                stud_id, name, age, gender, major, phone = student

            #Display the relevant student information
            print(f"{stud_id:<10} {name:<16} {phone:<15} {major:<5}")

def showStudentID(ID):
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Selects a student based on their ID
        cursor.execute("SELECT * FROM Student WHERE id = ?", (ID,))

        #Header
        printPage("StudentRecord.txt")
        print(f"{'ID':<10} {'Name':<16} {'Phone':<15} {'Major':<5}")
        student = cursor.fetchone()

        #Unpack student into multipel variables
        stud_id, name, age, gender, major, phone = student

        
        #Display the relevant student information
        print(f"{stud_id:<10} {name:<16} {phone:<15} {major:<5}")

def modifyStudent(ID, age, major, phone):
    #Connects to database
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Inserts modified student information into the database
        cursor.execute("UPDATE Student SET age = ?, major = ?, phone = ? WHERE id = ?",
                       (age, major, phone, ID))
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
        printPage("StudentRecord.txt")
        print(f"{'ID':<8} {'Name':<15} ") #Note: the student's classes need to be added

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
        printPage("StudentRecord.txt")
        print(f"{'ID':<8} {'Name':<15} ") #Note: the student's classes need to be added

        #Displays student scores
        students = cursor.fetchall()
        for student in students:
            print(student) #Note: needs formatting so it doesn't just show the raw data
        print()
