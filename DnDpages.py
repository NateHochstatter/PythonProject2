from DnDDatabaseFunctions import *
from allChecks import *

def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close()

def startPage():
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
                displayAllPage()
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
                validItem = True
            else:
                print("Invalid student ID")
        except:
            print("Invalid student ID")

    Name = str(input("Please enter the Character Name: "))

    validItem = False
    while validItem == False:
        try:
            Class = str(input("Please enter the Character Class: "))
            if checkClass(Class) == True:
                check = False
            else:
                print(f"\u274c Invalid Character Class")
        except:
            print(f"\u274c Invalid Character Class")

    validItem = False
    while validItem == False:
        try:
            Level = input(int("Please enter the Character Level: "))
            if checkLevel(Level) == True:
                check = False
            else:
                print(f"\u274c Invalid Character Level")
        except:
            rint(f"\u274c Invalid Character Level")

    validItem = False
    while validItem == False:
        try:
            Race = str(input("Please enter the Character Race: "))
            if checkRace(Race) == True:
                check = False
            else:
                print(f"\u274c Invalid Character Race")
        except:
            print(f"\u274c Invalid Character Race")

    Campaign = str(input("Please enter the Campaign: "))

    if finalcheck:
        newCharacter = {
            "ID": Id,
            "Name": Name,
            "Class": Class,
            "Level": Level,
            "Race": Race,
            "Campaign": Campaign}

        addCharacter(newCharacter)
        print("\u2714 New Character record has been added")

def deleteCharacterPage():
    try:
        #Prompt the user to enter a CharID to delete
        CharID = input("Please enter a Character ID to choose from: ")

    #Checks to make sure that the ID exists
        if(CharIDExists(CharID)==True): 
            displayCharacter(IDInput)
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
            else:
                print(f"\u274c Record not found")
    except:
        return

def displayCharacterPage():
    Id = str(input("Please enter the student ID: ")) #Get the id
    printPage("CharacterRecord.txt") #print the record text
    if checkValID(Id): #if statements to ensure the id is both valid and existing
        if IDExists(Id):
            displayCharacter(Id) #call the displayCharacter function with the given id
        else:
            print(f"\u274c The student Id {Id} does not exist") #error messages for if it is invalid or nonexistent
    else:
        print(f"\u274c The student Id {Id} is not valid")

def modifyCharacterPage():
    #starts off by basically doing the displayCharacter function but with a key change of setting a
    # check to false if there is an issue
    Id = str(input("Please enter the student ID: "))
    greatCheck = True #check for if there is an issue with the id which means it should stop
    # trying to modify something
    printPage("DndRecord.txt")
    if checkValID(Id):
        if IDExists(Id):
            displayCharacter(Id)
        else:
            print(f"\u274c The student Id {Id} does not exist")
            greatCheck = False
    else:
        print(f"\u274c The student Id {Id} is not valid")
        greatCheck = False

    if greatCheck: #if there were no issues continue as normal

        #A series of while loops that until a valid new data is given
        check = True
        while check:
            newName = str(input("New Name: "))
            if newName == "" or checkName(newName): #It is ok if the data is left empty or is just a valid name
                check = False
            else:
                print(f"\u274c Invalid Character Name")

        check = True
        while check:
            newClass = str(input("New Class: "))
            if newClass == "" or checkClass(newClass):
                check = False
            else:
                print(f"\u274c Invalid Character Class")

        check = True
        while check:
            newLevel = str(input("New Level: "))
            if newLevel == "" or checkLevel(newLevel):
                check = False
            else:
                print(f"\u274c Invalid Character Level")
        
        check = True
        while check:
            newRace = str(input("New Race: "))
            if newRace == "" or checkRace(newRace):
                check = False
            else:
                print(f"\u274c Invalid Character Race")

        check = True
        while check:
            newCampaign = str(input("New Campaign: "))
            if newCampaign == "":
                check = False
            else:
                print(f"\u274c Invalid Campaign")

        if newName == "" and newClass == "" and newLevel == "" and newRace == "" and newCampaign == "": #If they left all the inputs empty
            # send an error message
            print("\u274c Record not modified")
        else:
            #otherwise call the function and say things went well
            modifyCharacter(Id, newName, newClass, newLevel, newRace, newCampaign)
            print("\u2714 Character record updated successfully")


def CharIDExists(ID, filename="characterData.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        for characters in data:
            if character["ID"] == ID:
                return True
    return False 
