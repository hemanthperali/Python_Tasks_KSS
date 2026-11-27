'''Scenario:
Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

temps = np.array([28,30,32,31,29])

S = pd.Series(temps)
print("Series:")
print(S)

plt.plot(S)
plt.title("Temperature")
plt.grid(True,color = 'k')

plt.show()