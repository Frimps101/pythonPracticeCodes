#!python3
#A sort of program that asks user for a password 3 times before exiting
#Josephine Frimpomaa Kwakye
#9/14/2019 at 4:01



import sys

count = 0
password = 'Nyantekyiwaa'


print('You get three chances to enter the password')
for i in range(3):
    print('Enter password ' + str(i + 1))
    userInput  = input()
    count = count + 1

    if(count == 3 or userInput == ''):
        print('Sorry try again later')
        sys.exit()

    if(userInput == password):
        print('Congrats')
    else:
        print('You didnt get it right')



    
    


