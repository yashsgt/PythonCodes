# Write a recursive function to print all element in a list.
# Hint:-> Use list & index as parameter 


def print_list(list, idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)   # Jisme return value nahi hoga except base case usme function call hoga

fruits = ["Mango", "Litchi", "Apple", "Banana"]
print_list(fruits, 0)
