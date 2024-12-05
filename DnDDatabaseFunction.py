import sqlite3

def addCharacter(Stud_Id, Name, Class, Level, Race, Campaign):

    #Connects to the database
    with sqlite3.connect("Dnd.db") as conn:
        cursor = conn.cursor()

        #Inserts new student information into the database
        cursor.execute("INSERT INTO Dnd (Stud_Id, Name, Class, Level, Race, Campaign) VALUES (?, ?, ?, ?, ?, ?)",
                       (Stud_Id, Name, Class, Level, Race, Campaign))
    conn.commit()
    conn.close()

def showAllCharacters():
    with sqlite3.connect("Dnd.db") as conn:
        cursor = conn.cursor()

        #Selects all Characters
        cursor.execute("SELECT * FROM Dnd")

        characters = cursor.fetchall()

        #Header
        printPage("DndRecord.txt")
        print(f"{'CharId':<5} {'ID':<5} {'Name':<5} {'Class':<5} {'Level':<5} {'Race':<5} {'Campaign':<5}")

        #Iterate through every student
        for character in characters:

            #Unpack student into multiple variables
            char_id, stud, name, clas, level, race, campaign = character

            #Display the relevant student information
            print(f"{char_id:<10} {stud_id:<5} {name:<5} {clas:<5} {level:<5} {race:<5} {campaign:<5}")
        conn.close()

def showCharacter(element, value):
    #Connects to the database
    conn = sqlite3.connect("Dnd.db")
    cursor = conn.cursor()

    # Selects Character with a certain Id
    if element == "charId":
        cursor.execute("SELECT * FROM Dnd WHERE charId = ?", (int(value),))

    characters = cursor.fetchall()

    #Header
    printPage("DndRecord.txt")
    print(f"{'CharId':<5} {'ID':<5} {'Name':<5} {'Class':<5} {'Level':<5} {'Race':<5} {'Campaign':<5}")

    if characters:
        # Iterate through every character
        for character in characters:
            # Unpack character into multiple variables
            CharId, Id, Name, Class, Level, Race, Campaign = student

            # Display the relevant student information
            print(f"{CharId:<5} {Id:<11} {Name:<16} {Class:<5} {Level:<8} {Race:<8} {Campaign:<15}")
    conn.close()

def deleteCharacter(characterId):
    #Connects to the database
    with sqlite3.connect("Dnd.db") as conn:
        cursor = conn.cursor()

        #Deletes character information from the database
        cursor.execute("DELETE FROM Dnd WHERE characterId = ?", (characterId,))
        conn.commit()

#Function for modifying a characters elements
def modifyCharacter(ID, element, value):
    #Connects to database
    conn = sqlite3.connect("Dnd.db")
    cursor = conn.cursor()

    #if statements to check what is being modified
    if element == "name":
        # Inserts modified characters information into the database
        cursor.execute("UPDATE Dnd SET name = ? WHERE charId = ?", (value, int(ID)))
    if element == "class":
        cursor.execute("UPDATE Dnd SET class = ? WHERE charId = ?", (int(value), int(ID)))
    if element == "level":
        cursor.execute("UPDATE Dnd SET level = ? WHERE charId = ?", (int(value), int(ID)))
    if element == "race":
        cursor.execute("UPDATE Dnd SET race = ? WHERE charId = ?", (value, int(ID)))
    if element == "campaign":
        cursor.execute("UPDATE Dnd SET campaign = ? WHERE charId = ?", (value, int(ID)))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
