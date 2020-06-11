#!python3
#This is a guess the number game
#Ask the player to guess 6 times


import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#You will take a guess six times

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if(guess < secretNumber):
        print('Your guess is too low')
    elif(guess > secretNumber):
        print('Your guess is too high')
    else:
        break  #This condition is the correct guess!


if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guess')
else:
    print('Nope.The number i was thinking of was ' + str(secretNumber))
    
