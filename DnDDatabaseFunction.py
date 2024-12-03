import sqlite3

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
        print()
