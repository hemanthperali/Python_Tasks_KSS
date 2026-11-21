'''A dataset contains the following values:
[5, 10, 15, 20, 25, 30]
Scenario:
You want to distribute the data across 3 processors.
Task:
● Store the data in a NumPy array.
● Split it into 3 equal parts using NumPy.
'''

import numpy as np

arr1 = np.array([5,10,15,20,25,30])

split_data = np.split(arr1,3)

print("Splitted Data:",split_data)