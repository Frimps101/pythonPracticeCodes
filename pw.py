#! python3
#pw.py - An insecure python program...some sort of password manager


PASSWORDS = {"email":"evansofori12345","facebook":"nyantekyiwaa","udacity":"evansofori12345","Frimps":"thekwameinc","jo":"Nyantekyiwaa100",}

import sys,pyperclip


if len(sys.argv) < 2:
    print("Usage: pw.py[account] - copy account password")
    sys.exit()
    



account = sys.argv[1]   #first command line argument is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to the clipboard')
else:
    print('There is no account named ' + account)

