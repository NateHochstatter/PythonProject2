from allChecks import *

print("Names ")
print(checkName("hi")) #no caps and only one word
print(checkName("hi by")) #first letters aren't caps
print(checkName("Hi By")) #True
print(checkName("John Doe")) #True

print("Majors ")
print(checkMaj("cs")) #True
print(checkMaj("ddsacs")) #not a course

print("Phones ")
print(checkPhone("523535345")) #not a phone number
print(checkPhone("816 132 2132")) #missing -'s
print(checkPhone("815-342-4343")) #True

print("Age ")
print(checkAge(int("32"))) #True
print(checkAge(int("0"))) #out of range
print(checkAge(int("-32"))) #out of range
print(checkAge(int("322"))) #out of range

print("Gender ")
print(checkGender("o")) #True
print(checkGender("O")) #True
print(checkGender("M")) #True
print(checkGender("F")) #True
print(checkGender("f")) #True
print(checkGender("Fs")) #not a gender
print(checkGender("E")) #not a gender

print("Passwords ")
print(checkPassword("<PASSWORD>")) #no digit lower or special character
print(checkPassword("!vAlid2")) #True
print(checkPassword("VaL232d")) #no special character
print(checkPassword("!vAlid243434343434343")) #to long
print(checkPassword("!VAlid2")) #True
print(checkPassword("!vAliddSDS")) # no digit
print(checkPassword("!valid2")) #no upper

print("Usernames ")
print(checkUsername("John")) #True
print(checkUsername("john")) #first letter not upper
print(checkUsername("Jo3hn")) #digit
print(checkUsername("Johnassa")) #to long