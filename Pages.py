#Pages for all of the database functions

from DatabaseFunctions import *
from allChecks import *

def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close() #Close the connection

#function to start the login
def loginStartPage():

    #check while loop to get the option and do the action
    check = True
    while check:
        printPage("WelcomeLogin.txt")
        choice = input(str("Please Enter the Operation Code: "))  # get the users choice
        if choice == "1":
            loginPage()
        elif choice == "2":
            registerPage()
        elif choice == "3":
            check = False

#function for the login page
def loginPage():
    check = True  # check so it goes through the while loop until a valid id is given

    printPage("Login.txt")
    # the following series of while loops get a part of the students info only stopping if they get a valid input
    # or if the info already exists
    while check:
        username = str(input("Please enter your account: "))
        if exists("username", username):
            check = False
        else:
            print(f"\u274c Login failed. Account does not exist.")

    check = True
    while check:
        password = str(input("Please enter your password: "))
        if login(username, password):
            check = False
            startPage()
        else:
            print(f"\u274c Login failed. Invalid password.")

#function for the register page
def registerPage():
    printPage("RegisterName.txt")
    # the following series of while loops get a part of the students info only stopping if they get a valid input
    # or if the info already exists
    finalcheck = True  # Check for if the item already exists so it just stops and goes back to the start page
    check = True  # check so it goes through the while loop until a valid id is given

    # the following series of while loops get a part of the students info only stopping if they get a valid input
    # or if the info already exists
    while check and finalcheck:
        username = str(input("Please enter your account name: "))
        if checkUsername(username):
            if exists("username", username):
                print("\u274c Username already exists please try again.")
                finalcheck = False
            else:
                check = False
        else:
            print(f"\u274c Invalid Account Name")

    check = True
    if finalcheck:
        printPage("RegisterPassword.txt")
    while check and finalcheck:
        password = str(input("Please enter your password: "))
        if checkPassword(password):
            if exists("password", password):
                print("\u274c Password already exists please try again.")
                finalcheck = False
            else:
                check = False
                register(username, password)
        else:
            print(f"\u274c Invalid Password")

#Start page for the student menu
def startPage():
    #If statement and while loop to keep the program running until they select the leave option and confirm
    ex = False
    while (ex != True):
        printPage("WelcomeUser.txt")  # print the welcome text
        choice = input(str("Please Enter the Operation Code: "))  # get the users choice
        while (choice != "6"):
            #if statements for each option and the function correlating to them
            if (choice == "1"):
                addStudentPage()
            elif (choice == "2"):
                showStudentPage()
            elif (choice == "3"):
                modifyStudentPrompt()
            elif (choice == "4"):
                deleteStudentPage()
            elif (choice == "5"):
                scorePage()
            else:
                print("Wrong input enter a valid number") #error message
            printPage("WelcomeUser.txt") #Once the chosen function is done start the process again
            choice = input(str("Please Enter the Operation Code: "))
        leave = input(str("Do you want to return to previous menu? Enter Y to Confirm: "))
        if (leave.upper() == "Y"):
            ex = True

#Add Student Page
def addStudentPage():
    printPage("AddStudent.txt")

    #Variable for checking if input is valid
    validItem = False

    #Name
    while validItem == False:
        try:
            name = input("Please enter student's name (Firstname Lastname): ")

            #Checks if the name is valid
            if checkName(name) == True:
                validItem = True #Valid
            else:
                print("Invalid student name") #Invalid
        except:
            print("Invalid student name")#Error response

    #Age
    validItem = False
    while validItem == False:
        try:
            age = int(input("Please enter student's age: "))

            #Checks if age is valid
            if checkAge(age) == True:
                validItem = True
            else:
                print("Invalid student age")
        except:
            print("Invalid student age")#Error response

    #Gender
    validItem = False
    while validItem == False:
        try:
            gender = input("Please enter student's gender: ")

            #Checks if gender is valid
            if checkGender(gender) == True:
                validItem = True #Valid
            else:
                print("Invalid student gender") #Invalud
        except:
            print("Invalid student gender") #Error response

    #Major
    validItem = False
    while validItem == False:
        try:
            major = input("Please enter student's major: ")

            #Checks if major is valid
            if checkMaj(major) == True:
                major = major.upper()
                validItem = True #Valid
            else:
                print("Invalid student major") #Invalid
        except:
            print("Invalid student major") #Error response

    #Phone
    validItem = False
    while validItem == False:
        try:
            phone = input("Please enter student's phone number: ")

            #Checks if phone number is valid
            if checkPhone(phone) == True:
                validItem = True #Valid
            else:
                print("Invalid student major") #Invalid
        except:
            print("Invalid student major") #Error response

    #Add the student to the student database
    addStudent(name, age, gender, major, phone)
    print("Student added successfully!")

    try:
        userInput = int(input("1. Continue\n2. Exit\nPlease Enter 1 or 2: "))

        #1: The user will create another student
        if userInput == 1:
            addStudentPage()
        #2/Invalid: The user will exit the addStudentPage
        else:
            return

    except:
        return

def showStudentPage():

    try:
        printPage("ShowStudent.txt")
        choice = int(input("Make a selection: "))

        #1. Show all students
        if choice == 1:
            if studentsExist():
                showAllStudents()

        #2. Show students by name
        elif choice == 2:
            try:
                name = input("Enter a student name: ")

                if exists("name", name):
                    showStudent("name", name)
                else:
                    print("No student found")
            except:
                print("No student found")

        #3. Show student by ID
        elif choice == 3:
            try:
                ID = input("Enter a student ID: ")

                if exists("id", ID):
                    showStudent("id", ID)
                else:
                    print("No student found")
            except:
                print("No student found")
        else:
            return

    except:
        return

def modifyStudentPrompt():

    try:
        ID = input("Enter Student ID to modify: ")

    except:
        print("No record found")

    if exists("id", ID) == True:
        modifyStudentPage(ID)
    else:
        print("No record found")

def modifyStudentPage(ID):

    #Variable for checking if input is valid
    validItem = False

    #Age
    while validItem == False:
        try:
            newAge = int(input("Enter student's age: "))

            #Determine if the selected age is valid
            if checkAge(newAge) != True:
                #Invalid
                print("Invalid student age")
            else:
                #Valid
                validItem = True
        except:
            print("Invalid student age")

    #Major
    validItem = False
    while validItem == False:
        try:
            newMajor = input("Enter student's major: ")

            #Determine if the selected major is valid
            if checkMaj(newMajor) != True:
                #Invalid
                print("Invalid student major")
            else:
                #Valid
                validItem = True
                newMajor = newMajor.upper()
        except:
            print("Invalid student major")

    #Phone
    validItem = False
    while validItem != True:
        try:
            newPhone = input("Enter student's phone number: ")

            #Determine if the selected major is valid
            if checkPhone(newPhone) == False:
                #Invalid
                print("Invalid phone number")
            else:
                #Valid
                validItem = True
        except:
            print("Invalid phone number")

    modifyStudent(ID, newAge, newMajor, newPhone)
    print("Record modified successfully!")


def deleteStudentPage():
    try:
        printPage("Delete.txt")
        choice = int(input("Make a selection: "))

        #1. Delete students by name
        if choice == 1:
            name = input("Enter a student name to delete: ")
            if nameExists(name):
                deleteStudentName(name)
                print("Record deleted succesfully!")
            else:
                print("No record found")

        #2. Delete student by ID
        elif choice == 2:
            ID = int(input("Enter a student ID to delete: "))
            if IDExists(ID):
                deleteStudentID(ID)
                print("Record deleted successfully!")
            else:
                print("No record found")

        #Other: Return to main menu
        else:
            return
    except:
        return

def scorePage():
    #Selection Page
    try:
        printPage("StudentScore.txt")
        choice = int(input("Make a selection: "))

        #1. Display Student Score by Name
        if choice == 1:
            try:
                name = input("Enter student name to display scores: ")
                if nameExists(name):
                    showScore(name)
                else:
                    print("No record found")
            except:
                print("No record found")

    #2. Update Student Score by ID
        elif choice == 2:

            #Makes sure the ID is a valid input
            validID = False
            try:
                #ID to see which student grade should be changed
                ID = int(input("Enter student ID to update scores: "))
                validID = True

            except:
                print("No record found")

            #Only searches for ID if error was not thrown
            if validID == True:
                
                #ID Exists
                if IDExists(ID):

                    #Makes sure the course and grade inputs are valid
                    try:
                        course = input("Enter course to update score: ")
                        grade = int(input(f"Enter the new score for {course}: "))
                        modifyScore(ID, course, grade)

                    except:
                        print("Course either does not exist, or grade is invalid")
                        
            #ID does not exist
            else:
                print("No record found")
                
        #Other: Return to main menu
        else:
            return
                        
    except:
        return
