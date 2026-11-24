'''Ratings from different users:
ratings = np.array([2, 3, 4, 5, 1])
Task:
● Normalize ratings to a range 0 to 1 using:
normalized = (value - min) / (max - min)'''

import numpy as np

ratings = np.array([2,3,4,5,1])

min = np.min(ratings)
max = np.max(ratings)

normalize_arr = (ratings - min) / (max - min)

print("Original ratings:",ratings)
print("Normalize ratings:",normalize_arr)