#!python3 
# A simple password manager in python
# Followed from tutorials from the book "Automate The Boring Stuff With Python" by Al Sweigart
# Josephine Frimpomaa Kwakye  13:38


import sys,pyperclip

# pyperclip is a module used to copy things to the clipboard

passwords = {"email":"2345desraydtgfjpe","facebook":"123drt5yy78d3","github":"rfvhdgagsdsjh467"}

# First commandline argument is account name that is the key from the dictionary
account = sys.argv[1]

# First check the length of the password
if len(account) < 2:
    print("The argument length is less than two")
    sys.exit()


if account in passwords:
    pyperclip.copy(passwords[account])
    print("Your password has been copied to the clipboard")
else:
    print(passwords[account] + "doesn't exist")

