'''A company stores monthly sales data:
[10,20,30,40,50,60,70,80,90,100,110,120]
Scenario:
You need to display the data as 4 months × 3 products matrix.
Task:
● Convert the list to NumPy array.
● Reshape it into a 4 × 3 array.'''

import numpy as np

# Original list
l1 = [10,20,30,40,50,60,70,80,90,100,110,120]

# Convert original list into numpy array
arr1 = np.array([10,20,30,40,50,60,70,80,90,100,110,120])

# Reshape the original array
new_arr = arr1.reshape(4,3)

# Print the reshaped array
print("Reshaped array:\n",new_arr)