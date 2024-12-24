# Write a recursive function to print the check for palindrome string ?

def palindromestring(s):
    if(len(s)==1):
        return True
    else:
        if s[0] == s[-1]:

              return palindromestring(s[1:-1])
        else:
             return False
    
str = input("Enter a string : ")
if palindromestring(str):
     print("This is a palindrome")
else:
     print("This is not a palindrome")

     