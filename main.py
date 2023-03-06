# Part A:
def reverse_string(str):  
    str1 = ""   # Empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1 # Returns the reverse string to the function  
     
str = input ("Please Enter a string:")        
print("The First string was:",str)  
print("The new string is",reverse_string(str))  