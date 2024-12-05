import sqlite3
from DnDpages import *

def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close()

def addCharacter(Stud_Id, Name, Class, Level, Race, Campaign):
    #Connect to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #Inserts new character information into the database
    cursor.execute("INSERT INTO Dnd (studentId, name, class, race, level, campaign) VALUES (?, ?, ?, ?, ?, ?)",
                   (int(Stud_Id), Name, Class, Level, Race, Campaign))
    conn.commit()
    conn.close()

#print all created characters
def showAllCharacters():
    # Connect to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #Selects all Characters
    cursor.execute("SELECT * FROM Dnd")

    characters = cursor.fetchall()

    #Header
    printPage("DndRecord.txt")
    print(f"{'CharId':<9} {'ID':<11} {'Name':<15} {'Class':<12} {'Race':<12} {'Level':<5} {'Campaign':<15}")

    #Iterate through every character
    for character in characters:

        #Unpack character into multiple variables
        char_id, stud, name, clas, race, level, campaign = character

        #Display the relevant character information
        print(f"{char_id:<9} {stud:<11} {name:<15} {clas:<12} {race:<12} {level:<5} {campaign:<15}")
    conn.close()

#Print the character requested
def showCharacter(value):
    # Connect to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Selects Character with a certain Id
    cursor.execute("SELECT * FROM Dnd WHERE characterId = ?", (int(value),))

    characters = cursor.fetchall()

    #Header
    printPage("DndRecord.txt")
    print(f"{'CharId':<9} {'ID':<11} {'Name':<15} {'Class':<12} {'Race':<12} {'Level':<5} {'Campaign':<15}")

    # Iterate through every character
    for character in characters:
        # Unpack character into multiple variables
        char_id, stud, name, clas, race, level, campaign = character

        # Display the relevant character information
        print(f"{char_id:<9} {stud:<11} {name:<15} {clas:<12} {race:<12} {level:<5} {campaign:<15}")
    conn.close()

#Delete requested character
def deleteCharacter(characterId):
    # Connect to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #Deletes character information from the database
    cursor.execute("DELETE FROM Dnd WHERE characterId = ?", (characterId,))
    conn.commit()

#Function for modifying a characters elements
def modifyCharacter(ID, element, value):
    # Connect to the database
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    #if statements to check what is being modified
    if element == "name":
        # Inserts modified characters information into the database
        cursor.execute("UPDATE Dnd SET name = ? WHERE characterId = ?", (value, int(ID)))
    if element == "class":
        cursor.execute("UPDATE Dnd SET class = ? WHERE characterId = ?", (value, int(ID)))
    if element == "level":
        cursor.execute("UPDATE Dnd SET level = ? WHERE characterId = ?", (value, int(ID)))
    if element == "race":
        cursor.execute("UPDATE Dnd SET race = ? WHERE characterId = ?", (value, int(ID)))
    if element == "campaign":
        cursor.execute("UPDATE Dnd SET campaign = ? WHERE characterId = ?", (value, int(ID)))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
