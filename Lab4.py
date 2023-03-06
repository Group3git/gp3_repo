#program containing a function to 
# check if a user inputted number 
# is prime.

num = int(input("Enter a number:")) #Input number to be determine if prime or not

flag = False

if num == 1: # if num = to odd number then it is not prime
    print(num, "is not a prime number")
elif num > 1: # if num is greater than 1 check if number is prime
    for i in range(2, num):
        if (num % i) == 0:
            flag = True # if true then number is not prime
            break
    if flag == True: # checks flag
        print(num, "is not a prime number") # if flag is true print
    else:
        print(num, "is a prime number") # if flag is false print