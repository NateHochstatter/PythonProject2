import json

#Function to add a new character
def addCharacter(newCharacter, filename="characterData.json"):
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the json
        data.append(newCharacter) #Adds the new characters data to the json info

    with open(filename, 'w') as file:
        json.dump(data, file) #Writes the new json info with the new student to the file

#Function to find the index of the character with the given id
def findCharacter(ID, filename="characterData.json"):
    count = 0 #Made a count variable
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each character
        for character in data:
            if character["ID"] == ID: #Checks if the character ID is the one being looked for
                #If it is return the count to act as an index otherwise increase count
                return count
            else:
                count += 1

#Function to display the character with a given id
def displayCharacter(ID, filename="characterData.json"):
    index = findCharacter(ID) #Call the findCharacter function to get the index of the character
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the json
    #Print the info of the selected character in an organized manner
    print("Id: " + str(data[index]["ID"]) + " Name: " + str(data[index]["CharacterName"]) + " Class "
          + str(data[index]["Class"]) + " Level " + str(data[index]["Level"]) + " Race " + str(data[index]["Race"])
          + " Campaign " + str(data[index]["Campaign"]))

#Function to display all character in the file
def displayAllCharacters(filename="characterData.json"):
    #Note all prints for this function are formated for consistent look
    print(f"{'ID':<8} {'Name':<15} {'Class':<15} {'Level':<4} {'Race':<10} {'Campaign':<30}") #Print header for the table
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each character
        for character in data:
            # Print the info of each character as it loops through them
            print(f"{str(character["ID"]):<8} {str(character["CharacterName"]):<15} "
                  f"{(str(character["Class"])):<15} {(str(character["Level"])):<4} "
                  f"{(str(character["Race"])):<10} {(str(character["Campaign"])):<30}")

#Function to modify a character data
def modifyCharacter(oldID, newClass, newLevel, newRace, newCampaign, filename="characterData.json"):
    index = findCharacter(oldID) #Call the findCharacter function to get the index of the character
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the json
    #A series of if statements to check if they wanted to modify the element being checked
    #If a new element was provided then it sets the old element of the character at the index to the new one
    if newLevel != "":
        data[index]["Class"] = newClass
    if newLevel != "":
        data[index]["Level"] = newLevel
    if newRace != "":
        data[index]["Race"] = newRace
    if newCampaign != "":
        data[index]["Campaign"] = newCampaign
    with open(filename, 'w') as file:
        json.dump(data, file) #Writes the updated character info to the json

def CharIDExists(ID, filename="characterData.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        for characters in data:
            if character["ID"] == ID:
                return True
    return False 
