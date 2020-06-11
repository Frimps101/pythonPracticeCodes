#!python3
#A simple password locker


import sys,pyperclip

passwords = {"facebook":"Nyantekyiwaa","email":"evansofori12345","udemy":"nyantekyiwaa100"}

if len(sys.argv) < 2:
    print("Password length should be more than two")
    sys.exit()


account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password has been pasted to the clip board")
else:
    print("Incorrect password")

    