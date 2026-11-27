'''Scenario:
A shop records monthly sales:
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
Task:
● Convert data into a Pandas DataFrame
● Plot a line graph
● Label X-axis as months and Y-axis as sales'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([100,150,200,250,300])
months = ["Jan","Feb","Mar","Apr","May"]

df = pd.DataFrame({"Months":months,"Sales":sales})
print("DataFrame:\n",df)

plt.plot(df["Months"],df["Sales"],marker = 'o')
plt.title("Line Graph")
plt.ylabel("Sales")
plt.xlabel("Months")
plt.show()