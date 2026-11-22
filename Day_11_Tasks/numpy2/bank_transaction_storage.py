'''A bank stores the transaction amounts of a customer in a list:
[1200, 500, 800, 1500]
Scenario:
● Convert the list into a NumPy array.
● Print the type of the object.
● Verify that it is a NumPy ndarray'''

import numpy as np

# Original list
ls = [1200,500,800,1500]

# Convert list to numpy array
arr = np.array([1200,500,800,1500])

#Print the type of the object
print("Type of object:",type(arr))

# Verify whether it is a NumPy ndarray
if type(arr):
    print("It is a numpy ndarray")
else:
    print("It is not a numpy array")

