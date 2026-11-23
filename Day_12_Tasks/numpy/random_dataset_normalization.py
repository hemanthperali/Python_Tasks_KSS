'''Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered value'''

import numpy as np

# Generate random float values between 0 and 1
arr = np.random.rand(8)

print("Original array:",arr)

# Normalize by multiplying with 100
normalize_arr = arr * 100

print("Normalized array:",normalize_arr)

# Filter values greater than 50
filter_arr = normalize_arr[normalize_arr > 50]

print("Filtered array:",filter_arr)

# Sort the filtered values
sort_arr = np.sort(filter_arr)
print("Sorted array:",sort_arr)


