'''Scenario:
A dataset:[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference.'''

import numpy as np

arr = np.array([10,20,30,40])

# Create copy of array
x = arr.copy()

# Modify the original array
arr[2] = 43

# Print the result
print("Original array:",arr)
print("After modifying original array:",arr)
print("Copy array:",x,"\n")

# Repeat with the view
y = arr.view()

print("Original array:",arr)
print("By using view:",y)