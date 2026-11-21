'''A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
'''

import numpy as np

arr1 = np.array([12,7,25,3,18,10])

sorted = np.sort(arr1)

splitted = np.split(arr1,2)

sum1 = np.sum(splitted[0])
sum2 = np.sum(splitted[1])

print("Sorted Array:", sorted)
print("First Part:", splitted[0])
print("Second Part:", splitted[1])
print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)