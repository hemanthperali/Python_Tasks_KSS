'''You have:
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
Task:
● Count how many times each unique number appears.
● Return numbers with their counts.'''

import numpy as np

data = np.array([1,2,2,3,1,4,2,3])

import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

frequency = {}

for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)