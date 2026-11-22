'''A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically.'''

import numpy as np

# Original list
ls = ["Ravi","Anil","Sita","John"]

# Convert into numpy array
arr = np.array(["Ravi","Anil","Sita","John"])

# Sort the names alphabetically
new_arr = np.sort(arr)

# Print the new array
print("After sorting:",new_arr)