'''Scenario:
Monthly expenses:
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
Task:
● Create a pie chart
● Show percentage distribution'''

import numpy as np
from matplotlib import pyplot as plt

expenses = np.array([500,300,200])
labels = ["Food","Rent","Travel"]

plt.pie(expenses, labels = labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()