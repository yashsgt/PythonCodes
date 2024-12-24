import pandas as pd
stationary = ["Pen", "Pencil", "Eraser", "Cutter"]
s1 = pd.Series([10, 45, 34, 26], index = stationary)
s2 = pd.Series([234, 454, 675, 124], index = stationary)
print(s1 + s2)

