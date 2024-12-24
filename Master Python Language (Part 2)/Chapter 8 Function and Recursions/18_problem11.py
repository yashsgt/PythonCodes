# WAF to print the Odd numbers in reverse order ?

def countOdd(current_value, range):
    if(current_value>range):
        return
    countOdd(current_value+1, range)
    if(current_value%2==1):
        print(current_value)


range = int(input("Enter your range : "))
countOdd(1, range)