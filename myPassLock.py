#!python3
#Josephine Frimpomaa Kwakye
#12th September 2019, 8:00AM
#A simple immature password locker manager

import sys,pyperclip

PASSWORDS = {'email':'evansofori12345','Frimps':'Nyantekyiwaa','Frimps':'TheKwameInc'}



if len(sys.argv )< 2:
    print("Enter more than two characters")
    sys.exit()

account = sys.argv[1]

if(account in PASSWORDS):
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + "has been copied to the clipboard")
else:
    print("The account you entered does not exist")
    



