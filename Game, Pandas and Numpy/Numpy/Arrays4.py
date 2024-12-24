# Numpy Arrays consumes less memory as compared to lists

import numpy as np
import sys

# declaring a list of 1000 elements
s = range(1000)

# printing size of each element of the list
print("size of each element of list in bytes: ", sys.getsizeof(s))
print("size of whole list in bytes: ", sys.getsizeof(s)*len(s))

# declaring a Numpy array of 1000 element
D = np.arange(1000)

print("size of each element in numpy in bytes: ", D.itemsize)
print("size of the whole numpy array in bytes: ", D.size*D.itemsize)

