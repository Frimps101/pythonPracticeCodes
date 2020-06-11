# Write a function named collatz() that has one parameter
#If number is even then collatz() should print number number//2 and return this value
#If the numer is odd, then collatz() should print and return 3*number + 1


def collatz(number):
    if(number%2 == 0):
        return number // 2
    elif(number%2 == 1):
        return (3*number + 1)




def doUntilReturn1():
    while(True):
        print("Type an integer")
        userInput = int(input())
        if collatz(userInput) == 1:
            break
    return 1



print(doUntilReturn1())  
        
       

