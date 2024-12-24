# Write a recursive function to print the string in reverse order ?
def reverse_str(str1):
    if len(str1) == 1:
        return str1
    else:
        return reverse_str(str1[1:]) + str1[0]

str1 = input("Enter the string : ")
str2 = reverse_str(str1)
print("Reversed string is : ", str2)

