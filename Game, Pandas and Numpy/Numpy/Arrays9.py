# Numpy also provides the way to create an array by using the existing data by using the existing data
# By using: numpy.asarray()

import numpy as np
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.asarray(l1)
print(type(arr))
print(arr)


l2 = [[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]]    # The sublists which u provides must be of the same length
b = np.asarray(l2)
print(type(b))
print(b)


l3 = [(1, 2, 3), (4, 5, 6)]
c = np.array(l3)
print(type(c))
print(c)