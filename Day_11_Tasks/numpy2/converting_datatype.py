'''A shop stores product prices:
[10.5, 20.8, 15.3]
Scenario:
The billing system requires integer values.
Task:
● Convert the array from float to integer using astype()'''

import numpy as np

# Given float values
floats = np.array([10.5,20.8,15.3])

# Convert the array into integer 
new_arr = floats.astype('i')

# Print the values
print("Integer values:",new_arr)