'''A dataset:
arr = np.array([10, 25, 30, 15, 40])
Task:
● Convert to Pandas Series
● Filter values greater than 20'''

import pandas as pd
import numpy as np

arr = np.array([10,25,30,15,40])

# Convert the array into Series
s1 = pd.Series(arr)

filter_values = s1[s1 > 20]

print("Series:\n",s1)
print("Filtered Values :\n",filter_values)