'''A dataset:
data = np.arange(1, 13)
Task:
● Reshape it into a 3×4 matrix
● Compute average of each row'''

import numpy as np

data = np.arange(1,13)

reshape_arr = data.reshape(3,4)

avg = np.mean(reshape_arr,axis = 1)

print("Reshaped data:",reshape_arr)
print("Average :",avg)