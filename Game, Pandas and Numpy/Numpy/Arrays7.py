# Numpy array can be created in different ways:
# 1. Using numpy.empty()
# Syntax: numpy.zeros(shape, dtype= , order = "C")

import numpy as np
arr = np.empty((3, 2),dtype=int,order='C')
print(arr)


