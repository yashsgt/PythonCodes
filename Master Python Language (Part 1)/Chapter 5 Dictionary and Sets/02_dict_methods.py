marks = {
    "Yash" : 100, "Shubham" : 98, "Rohan" : 92
}
print(marks.items())   # x.items() is used to get the dict items.....

print(marks.keys())    # x.keys() is used to get the key keys of dictionary.....

print(marks.values())    # x.values() is used to get the values of the dictionary.....

print(marks.update({"Shubham" : 100}))     # x.update() is used to change or also add new the key-value pair from the dictionary.....

print(marks)

print(marks.get("Yash2"))     # Prints None
print(marks["Yash2"])      # Prints error
print(marks)

print(marks.pop("Shubham", 100))   #  x.pop("key", value) is used to remove the taken value in key-value pair.....
print(marks)

print(marks.popitem()) # x.popitem() is used to remove any key-value pair or we can say at the end from the dictionary it
# is removed.....
print(marks)




