#Modify Student Page

from allChecks import *
from DatabaseFunctions import *

def modifyStudentPrompt():

    try:
        ID = input("Enter Student ID to modify: ")

    except:
        print("No record found")

    if IDExists(ID) == True:
        modifyStudentPage(ID)
    else:
        print("No record found")

def modifyStudentPage(ID):

    #Variable for checking if input is valid
    validItem = False

    #Age
    while validItem == False:
        try:
            newAge = int(input("Enter student's age (press enter without modification): "))

            #Determine if the selected age is valid
            if checkAge(newAge) == False:
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
            newMajor = input("Enter student's major (press enter without modification): ")

            #Determine if the selected major is valid
            if checkMaj(newMajor) == False:
                #Invalid
                print("Invalid student major")
            else:
                #Valid
                validItem = True
        except:
            print("Invalid student major")

    #Phone
    validItem = False
    while validItem == False:
        try:
            newPhone = input("Enter student's phone number (press enter without modification): ")

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
