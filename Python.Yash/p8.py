n = int(input("enter value : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" "*(n-i),end="")
        print("*"*i)
