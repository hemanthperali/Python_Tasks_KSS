'''A warehouse stores product quantities:
[10, 20, 30, 40]
Task:
● Convert it into a NumPy array.
● Print the data type (dtype) of the array.'''

import numpy as np

# Original list
ls = [10,20,30,40]

# Convert original list into numpy array
arr = np.array([10,20,30,40])

# Print the data type 
print("Data type of array:",arr.dtype)