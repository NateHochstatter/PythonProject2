from DatabaseFunctions import *
from allChecks import *
from Pages import *

def loginStartPage():
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