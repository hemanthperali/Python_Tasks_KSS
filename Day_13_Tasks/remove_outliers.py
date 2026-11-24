'''Given data:
values = np.array([10, 12, 15, 18, 100, 14, 13])
Task:
● Compute the mean and standard deviation
● Remove values that are more than 2 standard deviations from the mean'''

import numpy as np

values = np.array([10,12,15,18,100,14,13])

# Calculate the mean and standard deviation
mean_values = np.mean(values)
std_values = np.std(values)

# Remove values more than 2 standard deviations from mean
filtered_values = values[np.abs(values - mean_values) <= 2 * std_values]

print("Mean:", mean_values)
print("Standard Deviation:", std_values)
print("Filtered values:", filtered_values)