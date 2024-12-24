import pandas as pd
data = [5, 6, 7, 8]
s = pd.Series(data)
dict1 = {"a":1,"b":2,"c":3}
s2 = pd.Series(dict1)
print("Series with list : ")
print(s)
print("Series with dictionary")
print(dict1)
print(s2)