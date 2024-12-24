# Write a recursive function to print the palindrome in python ?

def palindrome(M):
    if(len(M)<=1):
        return True
    else:
        if(M[-1]==M[0]):
            return palindrome(M[1:-1])
        else:
            return False

    
input_string = input("Enter a string :-> ")
if palindrome(input_string):
    print("This is a palindrome")
else:
    print("Not a palindrome")





    




    

