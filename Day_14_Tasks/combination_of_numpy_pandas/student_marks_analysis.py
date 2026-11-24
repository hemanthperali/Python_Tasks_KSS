'''Marks data:
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
Task:
● Convert into DataFrame with columns "Math", "Science"
● Add a new column Total
● Find student with highest total'''

import pandas as pd
import numpy as np

arr = np.array([
[80, 90],
[70, 60],
[85, 95]])

df = pd.DataFrame(arr, columns = ["Maths","Science"])

df["Total"] = df["Maths"] + df["Science"]

highest_mark = df.loc[df["Total"].idxmax()]

print("DataFrame:\n",df)
print("Highest Mark student:\n",highest_mark)