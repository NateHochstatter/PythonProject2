def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close() #Close the connection

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

                if nameExists(name):
                    showStudentName(name)
                else:
                    print("No student found")
            except:
                print("No student found")

        #3. Show student by ID
        elif choice == 3:
            try:
                ID = input("Enter a student ID: ")

                if IDExists(ID):
                    showStudentID(ID)
                else:
                    print("No student found")
            except:
                print("No student found")
        else:
            return

    except:
        return

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
