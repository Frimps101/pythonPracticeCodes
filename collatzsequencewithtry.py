#!python 3
#Automate the boring stuff with python
#This is a sort of continuation of collatz sequence but with try and except statement
#Input validation


def collatz(number):
    if (number%2 == 0):
        print(number // 2)
        return (number // 2)
    elif (number%2 == 1):
        print(3 * number + 1)
        return(3 * number + 1)

print("Enter any value")
value = int(input())

try:
    while(value != 1):
        value = collatz(value)
except ValueError:
    print("Invalid input type")


    
    
        

