'''A list contains roll numbers:
[101, 102, 103, 104, 105, 106]
Scenario:
You want only the middle students (index 2 to 4).
Task:
● Use NumPy slicing to extract those value'''

import numpy as np

# Original list
ls = [101,102,103,104,105,106]

# Convert the original list into numpy
arr1 = np.array([101,102,103,104,105,106])

# Extract the middle students
print("Middle Students:",arr1[2:4])