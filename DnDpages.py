from DatabaseFunctions import exists
from DnDDatabaseFunction import *
from DatabaseFunctions import *
from allChecks import *

def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close()

def startPageDnd():
    #If statement and while loop to keep the program running until they select the leave option and confirm
    ex = False
    while (ex != True):
        
        printPage("WelcomeDnD.txt")  # print the welcome text
        choice = input(str("Please Enter the Operation Code: "))  # get the users choice
        
        while (choice != "6"):
            #if statements for each option and the function correlating to them
            if (choice == "1"):
                addCharacterPage()
            elif (choice == "2"):
                deleteCharacterPage()
            elif (choice == "3"):
                modifyCharacterPage()
            elif (choice == "4"):
                displayCharacterPage()
            elif (choice == "5"):
                showAllCharacters()
            else:
                print("Wrong input enter a valid number") #error message
            
            printPage("WelcomeDnD.txt") #Once the chosen function is done start the process again
            choice = input(str("Please Enter the Operation Code: "))
        
        leave = input(str("Do you want to return to previous menu? Enter Y to Confirm: "))
        if (leave.upper() == "Y"):
            ex = True


def addCharacterPage():
    printPage("AddCharacter.txt")
    validItem = False 
    while validItem == False:
        try:
            Id = str(input("Please enter the student ID: "))
            if checkValID(Id) == True:
                if exists("id", Id):
                    validItem = True
                else:
                    print("Invalid student ID")
            else:
                print("Invalid student ID")
        except:
            print("Invalid student ID")

    Name = str(input("Please enter the Character Name: "))

    validItem = False
    while validItem == False:
        Class = str(input("Please enter the Character Class: "))
        if checkClass(Class):
            validItem = True
        else:
            print(f"\u274c Invalid Character Class")

    validItem = False
    while validItem == False:
        Level = str(input("Please enter the Character Level: "))
        if checkLevel(Level):
            validItem = True
        else:
            print(f"\u274c Invalid Character Level")

    validItem = False
    while validItem == False:
        Race = str(input("Please enter the Character Race: "))
        if checkRace(Race) == True:
            validItem = True
        else:
            print(f"\u274c Invalid Character Race")

    Campaign = str(input("Please enter the Campaign: "))

    addCharacter(Id, Name, Class, Race, Level, Campaign)
    print("\u2714 New Character record has been added")


def deleteCharacterPage():
    try:
        #Prompt the user to enter a CharID to delete
        CharID = input("Please enter a Character ID to choose from: ")

        if(exists("characterId" ,CharID)):
            #Checks to make sure that the ID exists
            showCharacter(CharID)
            #Verify that the user wants to delete the character
            response = input("Are you sure you want to delete this character from the record? Y or N: ")
                #Yes
            if response.lower() == "y":
                deleteCharacter(CharID)
                print(f"Character {CharID} has been deleted")
                 #No
            elif response.lower() == "n":
                    print(f"Character {CharID} has not been deleted")
                #Invalid responses
            else:
                print("INVALID RESPONSE")
    except:
        return

def displayCharacterPage():
    try:
        Id = str(input("Please enter the character ID: ")) #Get the id
        if exists("characterId", Id):
            showCharacter(Id)  # call the showCharacter function with the given id
        else:
            print(f"\u274c The character Id {Id} does not exist")  # error messages for if it is invalid or nonexistent
    except:
        return

def modifyCharacterPage():
    #starts off by basically doing the displayCharacter function but with a key change of setting a
    # check to false if there is an issue
    Id = str(input("Please enter the Character ID: "))
    greatCheck = True #check for if there is an issue with the id which means it should stop
    if exists("characterId", Id):
        showCharacter(Id)
    else:
        print(f"\u274c The character Id {Id} does not exist")
        greatCheck = False

    if greatCheck: #if there were no issues continue as normal

        #If the name is left blank do nothing otherwise modify it
        newName = str(input("New Name: "))
        if newName != "":
            modifyCharacter(Id, "name", newName)

        # A series of while loops that until a valid new data is given
        check = True
        while check:
            newClass = str(input("New Class: "))
            if newClass == "" or checkClass(newClass):
                check = False
                if newClass != "":
                    modifyCharacter(Id, "class", newClass)
            else:
                print(f"\u274c Invalid Character Class")

        check = True
        while check:
            newRace = str(input("New Race: "))
            if newRace == "" or checkRace(newRace):
                check = False
                if newRace != "":
                    modifyCharacter(Id, "race", newRace)
            else:
                print(f"\u274c Invalid Character Race")

        check = True
        while check:
            newLevel = str(input("New Level: "))
            if newLevel == "" or checkLevel(newLevel):
                check = False
                if newLevel != "":
                    modifyCharacter(Id, "level", newLevel)
            else:
                print(f"\u274c Invalid Character Level")

        newCampaign = str(input("New Campaign: "))
        if newCampaign != "":
            modifyCharacter(Id, "campaign", newCampaign)

        if newName == "" and newClass == "" and newLevel == "" and newRace == "" and newCampaign == "":
            #If they left all the inputs empty send an error message
            print("\u274c Record not modified")
        else:
            #otherwise say things went well
            print("\u2714 Character record updated successfully")
