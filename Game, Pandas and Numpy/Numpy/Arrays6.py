# Numpy Arrays support elementwise operations, Lists don't

import numpy as np
l1 =[1, 2, 3, 4, 5]
arr = np.array(l1)

l1 = l1 + 4       # list don't support element-wise operation
print("New list is: ", l1)


arr = arr + 4   # Array support element-wise operation
print("New array is: ", arr)


