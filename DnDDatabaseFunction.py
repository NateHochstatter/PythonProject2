import sqlite3

def showAllCharacters():
    with sqlite3.connect("Dnd.db") as conn:
        cursor = conn.cursor()

        #Selects all Characters
        cursor.execute("SELECT * FROM Dnd")

        characters = cursor.fetchall()

        #Header
        printPage("DndRecord.txt")
        print(f"{'ID':<5} {'CharId':<5} {'Name':<5} {'Class':<5} {'Level':<5} {'Race':<5} {'Campaign':<5}")

        #Iterate through every student
        for characters in characters:

            #Unpack student into multiple variables
            stud_id, char_id, name, clas, level, race, campaign = student

            #Display the relevant student information
            print(f"{stud_id:<10} {char_id:<5} {name:<5} {clas:<5} {level:<5} {race:<5} {campaign:<5}")
        print()
