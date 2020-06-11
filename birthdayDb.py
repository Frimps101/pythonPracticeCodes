#!python3
#A simple python program that asks user if enter their names 
#and if it doesnt exist in the database then it adds their 
#birthdays to the database
#Josephine Frimpomaa Kwakye



birthdays = {
    "Jo":"April 28",
    "Maxwell":"July 19",
    "Eugenia":"November 20",
    "Aunty Maggie":"October 25"
}


print("Please enter the name whose birthday you want to search for")
username = input()

if username in birthdays:
    print(birthdays[username] + " is the birthday of " + username)
else:
    print("It seems the name is not in the database")
    print("What is their birthday so that it can be added to the database")
    user_birthday = input()
    #birthdays[username] = user_birthday
    birthdays.setdefault(username,user_birthday)
    print("Your birthday has been added to the database. " \
        + "Have a nice day")




    
