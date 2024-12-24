# WAF to print the factorial of a number ?

def fact(x, prod):
    if(x==1):
        print(prod)
        return
    prod = prod * x
    fact(x-1, prod)


fact(5,1)
    