'''An IoT device records a single sensor reading = 75.
Task:
● Create a 0-D NumPy array with this value.
● Print the value and check its number of dimensions'''

import numpy as np

arr = np.array(75)

# Print the value
print("Value:",arr)

# Print the number of dimensions in array
print("Number of dimensions:",arr.ndim)
