import numpy as np
l = [1, 3, 2, 7, 5, 8]

# converting list to array
arr = np.asarray(l)
print("List:", l)
print("arr:", arr)

# made another array out of arr using asarray function
arr1 = np.asarray(arr)

# displaying arr1 before the changes made
print("arr1:", arr1)

# change made in arr1
arr1[4] = 22

# displaying arr1, arr, list after the change has been made
print("l:", l)
print("arr:", arr)
print("arr1:",arr1)


