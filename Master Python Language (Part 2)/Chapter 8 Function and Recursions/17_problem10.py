# WAF to print odd numbers according to user input ?

def countOdd(Current_value, range):
    if(Current_value>range):
        return
    if(Current_value%2 == 1):
        print(Current_value)
    countOdd(Current_value+1,range)

range = int(input("Enter range : "))
countOdd(1, range)