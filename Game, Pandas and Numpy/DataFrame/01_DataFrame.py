#Creating DataFrame from the list of Dictionary
import pandas as pd
import numpy as np
d1 = {"name" : "Ravi","age" : 45, "marks":100}
d2 = {"name" : "Raman","age" : 42, "marks":99}
data = [d1, d2]
df = pd.DataFrame(data)
print(df)

