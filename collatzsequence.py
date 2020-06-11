#!python3
# Projects from automating the boring stuff with python
# A function named collatz that has one parameter named number
# If number is even then collatz() should print number // 2
# If number  is odd then collatz() should print and return 3 * number + 1
# A program that lets user type in an integer and that
# keeps calling collatz from collatz sequence on that number until
# function returns 1



def collatz(number):
    if (number%2 == 0):
        print(number // 2)
        return (number // 2)
    elif (number%2 == 1):
        print(3 * number + 1)
        return(3 * number + 1)


print("Type in any integer")
integer = int(input())

while(integer != 1):
    integer = collatz(integer)
    



    
