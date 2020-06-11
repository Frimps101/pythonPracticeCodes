
birthdays = {"Max":"July 17","Lawlaw":"July 25","Jo":"April 28","Eugenia":"November 20","Araba":"October 3"}


while(True):
    print("Enter your name")
    your_name = input()
    if(your_name == " "):
       break

    if (your_name in birthdays):
       print("Your birthday is: "+ birthdays[your_name])
    elif(your_name not in birthdays):
         print("Your name is not here,we're  adding it to the database?")
         print("Enter your birthday")
         user_birthday = input()
         birthdays[your_name]=user_birthday
         print("Your name has been added to the database")
         break



