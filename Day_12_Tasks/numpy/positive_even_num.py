'''Scenario:
A dataset contains mixed values:
arr = [-5, 10, 15, -2, 20, 25, 30]
Task:
● Convert to NumPy array.
● Filter values that are:
○ Positive
○ Even
'''

import numpy as np

arr = np.array([-5,10,15,-2,20,25,30])

# Create empty list
filter_arr = []

# Loop through each element in array
for i in arr:
    # Check the element is positive and it is divisible by 2
    if i>0 and i%2==0:
        filter_arr.append(i)

new_arr = np.array(filter_arr)

print("Filtered array:",new_arr)

