# 2. Using numpy.zeros()
# Syntax: numpy.zeros(shape, dtype = float, order = 'C')

import numpy as np
arr = np.zeros((3, 3),dtype=int,order='C')
print(arr)
print("\n")

# 3. Using numpy.ones()
# Syntax: numpy.ones(shape, dtype = float, order = 'C')     In dtype you can take anything (like int, float, etc.)
arr = np.ones((4, 3),dtype=int,order='F')
print(arr)
print("\n")


# 4. Using numpy.full()
# Syntax: numpy.full(shape, fill_value, dtype=None, order = 'C')
arr = np.full((3, 3),100,dtype=int,order='C')
print(arr)
print("\n")


# 5. Using numpy.arange()
# Syntax: numpy.arange((start,end,step),dtype= )
arr = np.arange(2, 6, 1,dtype=int)
print(arr)  # The advantage of numpy.arange() over the normal in-built range() function is that it allows us to generate sequences of numbers that are not integers.


