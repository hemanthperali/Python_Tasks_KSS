'''An e-commerce website stores product ratings:
[4, 5, 3, 4, 2]
Task:
● Convert it to a NumPy array.
● Print the first and last rating using indexing.'''

import numpy as np

# Original List
ls = [4,5,3,4,2]

# convert the original list into numoy array
arr = np.array([4,5,3,4,2])

# Access the first rating value
print("First Rating:",arr[0])

# Access the last rating value
print("Last Rating:",arr[-1])
