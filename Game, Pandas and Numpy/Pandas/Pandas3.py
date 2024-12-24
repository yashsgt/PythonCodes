# Series
import numpy as np
import pandas as pd
list1 = [1, 2, 3, 2, 4, 1, 5, 6, 7]
s1 = pd.Series(list1)
print("Mean of s1 ", s1.mean())
print("Mode of s1 ", s1.mode())
print("std of s1 ", s1.std())
print("Count value of s1 ", s1.value_counts())
print("Max of s1", s1.max())
print("Min of s1 ", s1.min())
print("sum of s1 ", s1.sum())
print("Index max of s1 ", s1.idxmax())
print("Index min of s1 ", s1.idxmin())
print("Describe of s1 ", s1.describe())
print("First three value \n", s1.head(3))
print("Last three value \n", s1.tail(3))
