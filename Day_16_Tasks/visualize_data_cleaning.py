'''Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = np.array([100,np.nan,200,150,np.nan,300])

S = pd.Series(data)
print(S)

avg = np.mean(S)
print("Average:",avg)

cleaned_data = S.fillna(avg)
print("Cleaned Data:")
print(cleaned_data)

plt.figure(figsize=(10, 4))

# Line graph of cleaned data
plt.subplot(1, 2, 1)
plt.plot(cleaned_data, marker='o')
plt.title("Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

# Bar chart of values greater than average
plt.subplot(1, 2, 2)
filtered_data = cleaned_data[cleaned_data > avg]
plt.bar(filtered_data.index, filtered_data)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.show()

