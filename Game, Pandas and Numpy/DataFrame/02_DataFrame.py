# Creating DataFrame from the dictionary of Series

import pandas as pd
name = ["Ravi","Sam","Kuna"]
age = [23, 43, 34]
ser_name = pd.Series(name)
ser_age = pd.Series(age)
data = {"Name":ser_name, "Age":ser_age}
df = pd.DataFrame(data)
print("Students details")
print(df)