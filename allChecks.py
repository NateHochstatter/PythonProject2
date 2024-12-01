
# Function for checking the username
def checkUsername(username):
    # While loop to check that there are no digits
    i = 0
    while i < len(username):
        if username[i].isdigit():
            return False
        i += 1

    #if statement to check if the username length is valid and its first letter is uppercase
    if 3 <= len(username) <= 6 and username[0].isupper():
        return True
    else:
        return False

# Function for checking the password
def checkPassword(password):
    # Set of the special characters
    special = ["!", "@", "#", "$", "%", "^", "&", "*"]

    #A set of checks for the relevant conditions
    upper = False
    lower = False
    digit = False

    #if statements to check the length and the first letter
    if 6 <= len(password) <= 12 and password[0] in special:
        #a while loop to go through and check there is 1 uppercase, lowercase, and digit
        i = 1
        while i < len(password):
            if password[i].isupper() and not upper:
                upper = True
            elif password[i].islower() and not lower:
                lower = True
            elif password[i].isdigit() and not digit:
                digit = True
            i += 1
        #If all the conditions are met return true else return false
        if upper and lower and digit:
            return True
        else:
            return False
    else:
        return False


# Function for checking the name
def checkName(name):
    #While loop to check that there are no digits
    i = 0
    while i < len(name):
        if name[i].isdigit():
            return False
        i += 1

    # Split the name into first and last names
    name_parts = name.split()

    # Check if there are exactly two parts: first name and last name
    if len(name_parts) != 2:
        return False

    first_name, last_name = name_parts

    # Check that both first and last name are at least 2 letters long
    if len(first_name) < 2 or len(last_name) < 2:
        return False

    # Check if the first letter of each name is capitalized and the rest are lowercase
    if not (first_name[0].isupper() and first_name[1:].islower()):
        return False
    if not (last_name[0].isupper() and last_name[1:].islower()):
        return False

    return True


# Function for checking the Phone
def checkPhone(phone):
    # Check that the length is exactly 12 characters
    if len(phone) != 12:
        return False

    # Check if the correct positions contain dashes
    if phone[3] != '-' or phone[7] != '-':
        return False

    # Check if the rest of the characters are digits
    if not (phone[:3].isdigit() and phone[4:7].isdigit() and phone[8:].isdigit()):
        return False

    return True


# Function for checking the Major
def checkMaj(inp):
    # Set made of the Majors in Computer Science
    Majors = ["CS", "CYBR", "SE", "IT", "DS"]

    # Check if the Major is valid in the set of majors
    if (inp.upper() in Majors):
        return True
    else:
        return False

# Function for checking the age
def checkAge(age):
    #if statement to check the age
    if 0 < age < 100:
        return True
    else:
        return False

# function for checking the gender
def checkGender(gender):
    #if statement to check if the gender is one of the 3 right answers
    if gender.upper() in ["M", "F", "O"]:
        return True
    else:
        return False

