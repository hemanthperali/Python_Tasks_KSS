'''A dataset:
arr = np.array([10, np.nan, 30, np.nan, 50])
Task:
● Convert to Pandas Series
● Replace NaN values with the mean of the Series
● Print updated data'''

import pandas as pd
import numpy as np

arr = np.array([10,np.nan,30,np.nan,50])

s = pd.Series(arr)

avg = s.mean()

res = s.fillna(avg)

print("Updated result:\n",res)