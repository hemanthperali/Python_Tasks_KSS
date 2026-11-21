'''An image processing system stores pixel intensity values in a matrix.
Scenario:
[[1, 2],
[3, 4]]
Task:
● Create a NumPy array for this matrix.
● Find its transpose.
● Print both matrices'''

import numpy as np

arr1 = np.array([[1,2],[3,4]])

print("Original matrix:",arr1)

res = np.transpose(arr1)

print("Transpose Matrix:",res)