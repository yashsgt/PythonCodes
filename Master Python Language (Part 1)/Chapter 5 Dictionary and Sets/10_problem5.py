# Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names.
#  Assume that the names are uniques ?

d = {}

name = input("Enter friends name : " )
lang = input("Enter Language : ")
d.update({name : lang})

name = input("Enter friends name : " )
lang = input("Enter Language : ")
d.update({name : lang})

name = input("Enter friends name : " )
lang = input("Enter Language : ")
d.update({name : lang})

name = input("Enter friends name : " )
lang = input("Enter Language : ")
d.update({name : lang})

print(d)

