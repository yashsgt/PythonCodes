# Numpy arrays are fast as compared to python lists.

import numpy as np
import array as arr
import time

size = 1000000
list1 = range(size)
list2 = range(size)

arr1 = np.arange(size)
arr2 = np.arange(size)

# capturing time before multiplication of python lists
initialTime = time.time()

# multiplying elements of the lists and stored in another list
resultantList = [(a*b) for a, b in zip(list1, list2)]

# calculating execution time
print("Time taken by list to perform multiplication: ", (time.time()-initialTime),"seconds")


# capturing time before the multiplication of Numpy arrays
initialTime = time.time()

# multiplying elements of both Numpy arrays
resultantArray = arr1 * arr2

# calculating execution time
print("Time taken by the Numpy Arrays to perform multiplication: ",(time.time()-initialTime),"seconds")







