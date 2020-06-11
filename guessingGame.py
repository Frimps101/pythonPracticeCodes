#!python3
#My take on a guessing game


import random

secretNumber = random.randint(2,20)
print('I am thinking of a number between 2 an 20')
print('You will be guessing four times'



for guessesTaken in range(1,4):
      print('Take a guess')
      guess = int(input())

      if guess < secretNumber:
          print('Your guess is too low')
      elif guess > secretNumber:
          print('Your guess is too high')
      else:
          break



if guess == secretNumber:
    print('Congrats, you guessed the number correctly. You took ' + str(guessesTaken) + 'guesses')
else:
    print('No you didnt get it but you took ' + str(guessesTaken) + 'guesses')
    
      
      
