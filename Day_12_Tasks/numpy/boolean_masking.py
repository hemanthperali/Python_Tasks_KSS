'''Scenario:
Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition'''

import numpy as np

# Employee Salaries
arr = np.array([25000,40000,15000,50000,30000])

# Filter salaries above 30000
filter_arr = arr[arr>30000]

# Count employees satisfying the condition
count = len(filter_arr)

print("Salaries above 30000:",filter_arr)
print("Number of employees:",count)