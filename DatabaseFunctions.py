import sqlite3
from Pages import *

def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close() #Close the connection
    
#Function to check if an element exists
def exists(element, value):

    #connect to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #If statements for the elements you are looking for
    if element == "phone":
        cursor.execute("SELECT * FROM Student WHERE phone = ?", (value,))
    if element == "name":
        cursor.execute("SELECT * FROM Student WHERE name = ?", (value,))
    if element == "username":
        cursor.execute("SELECT * FROM User WHERE username = ?", (value,))
    if element == "password":
        cursor.execute("SELECT * FROM User WHERE password = ?", (value,))
    if element == "id":
        cursor.execute("SELECT * FROM Student WHERE id = ?", (int(value),))
    if element == "scoreId":
        cursor.execute("SELECT * FROM Score WHERE id = ?", (int(value),))
    if element == "scoreName":
        cursor.execute("SELECT * FROM Score WHERE name = ?", (value,))
    if element == "characterId":
        cursor.execute("SELECT * FROM Dnd WHERE characterId = ?", (int(value),))
    students = cursor.fetchall()

    #if statement to check the results.
    if students:
        conn.close()
        return True
    else:
        conn.close()
        return False

#Function for registering a new user
def register(username, password):
    # Connects to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Inserts new student information into the database
    cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)",
                   (username, password))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

#function for login
def login(username, password):
    #connect tp database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #search the database for the user
    cursor.execute("SELECT * FROM User WHERE username = ? AND password = ?", (username, password))

    user = cursor.fetchall()

    #check the results
    if len(user) == 0:
        return False
    else:
        return True

#Function to add a student
def addStudent(name, age, gender, major, phone):

    #Connects to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #Inserts new student information into the database
    cursor.execute("INSERT INTO Student (name, age, gender, major, phone) VALUES (?, ?, ?, ?, ?)",
                   (name, int(age), gender, major, phone))
    # Commit changes and close the connection
    conn.commit()
    conn.close()

#function to show all students
def showAllStudents():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #Selects all students
    cursor.execute("SELECT * FROM Student")

    students = cursor.fetchall()

    #Header
    printPage("StudentRecord.txt")
    print(f"{'ID':<11} {'Name':<16} {'Age':<5} {'Gender':<8} {'Major':<8} {'Phone':<15}")

    #Iterate through every student
    for student in students:

        #Unpack student into multiple variables
        id, name, age, gender, major, phone = student

        #Display the relevant student information
        print(f"{id:<11} {name:<16} {age:<5} {gender:<8} {major:<8} {phone:<15}")
    conn.close()

#function to show a student using an element (name or id)
def showStudent(element, value):
    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    if element == "name":
        # Selects all students with a certain name
        cursor.execute("SELECT * FROM Student WHERE name = ?", (value,))
    if element == "id":
        # Selects a student based on their ID
        cursor.execute("SELECT * FROM Student WHERE id = ?", (int(value),))
    students = cursor.fetchall()

    #Header
    printPage("StudentRecord.txt")
    print(f"{'ID':<11} {'Name':<16} {'Age':<5} {'Gender':<8} {'Major':<8} {'Phone':<15}")

    if students:
        # Iterate through every student
        for student in students:
            # Unpack student into multiple variables
            id, name, age, gender, major, phone = student

            # Display the relevant student information
            print(f"{id:<11} {name:<16} {age:<5} {gender:<8} {major:<8} {phone:<15}")
    conn.close()

#Function for modifying a students elements
def modifyStudent(ID, element, value):
    #Connects to database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #if statements to check what is being modified
    if element == "age":
        # Inserts modified student information into the database
        cursor.execute("UPDATE Student SET age = ? WHERE id = ?", (int(value), int(ID)))
    if element == "gender":
        cursor.execute("UPDATE Student SET gender = ? WHERE id = ?", (value.upper(), int(ID)))
    if element == "major":
        cursor.execute("UPDATE Student SET major = ? WHERE id = ?", (value.upper(), int(ID)))
    if element == "phone":
        cursor.execute("UPDATE Student SET phone = ? WHERE id = ?", (value, int(ID)))
    if element == "name":
        cursor.execute("UPDATE Student SET name = ? WHERE id = ?", (value, int(ID)))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

#Deletes Students by name
def deleteStudentName(name):
    # Connects to database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #Deletes student information from the database
    cursor.execute("DELETE FROM Student WHERE name = ?", (name,))
    conn.commit()
    conn.close()

#Deletes students by ID
def deleteStudentID(ID):
    # Connects to database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Deletes student information from the database
    cursor.execute("DELETE FROM Student WHERE id = ?", (int(ID),))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


#function for showing a students scores
def showScore(name):
    # Connects to database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Selects students based on their name
    cursor.execute("SELECT * FROM Score WHERE name = ?", (name,))

    # Header
    printPage("StudentRecord.txt")
    print(f"{'ID':<12} {'Name':<15} {'CS_1030':<9} {'CS_1100':<9} {'CS_2030':<9}")

    # Displays student scores
    students = cursor.fetchall()
    for student in students:
        # Unpack student into multiple variables
        id, name, CS_1030, CS_1100, CS_2030 = student

        # Display the relevant student information
        print(f"{id:<12} {name:<15} {CS_1030:<9} {CS_1100:<9} {CS_2030:<9}")
    conn.close()

#Function for modifying a students scores
def modifyScore(Id, element, value):
    # Connects to database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # if statements to check what is being modified
    if element == "CS_1030":
        # Inserts modified student information into the database
        cursor.execute("UPDATE Score SET CS_1030 = ? WHERE id = ?", (int(value), int(Id)))
    if element == "CS_1100":
        cursor.execute("UPDATE Score SET CS_1100 = ? WHERE id = ?", (int(value), int(Id)))
    if element == "CS_2030":
        cursor.execute("UPDATE Score SET CS_2030 = ? WHERE id = ?", (int(value), int(Id)))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def studentsExist():

    #Connects to the database
    with sqlite3.connect("school.db") as conn:
        cursor = conn.cursor()

        #Search for Students in the database
        cursor.execute("SELECT * FROM Student")

        student = cursor.fetchone()

        #Determine if student exists
        if student:
            return True #Does exist
        else:
            return False #Does not exist


